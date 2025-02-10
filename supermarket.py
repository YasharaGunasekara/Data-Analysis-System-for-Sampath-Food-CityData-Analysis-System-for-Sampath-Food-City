import matplotlib.pylab as plt
import pandas as pd
from abc import ABC, abstractmethod

# Abstract class - Analysis
class Analysis(ABC):
    @abstractmethod
    def performAnalysis(self):  # Abstract method
        pass


# Branch Analysis - Analysis by branch
class BranchAnalysis(Analysis):
    def performAnalysis(self):
        # Load data set into panda frame
        df = pd.read_csv('C:/Users/USER/AppData/Local/Programs/Python/Python313/supermarket.csv')
        
        # Summarize filtered data to find total quantity for each branch
        result = df.groupby('Branch')['Quantity'].sum().reset_index()
        print(result)  # Print summary

        # Draw Bar Chart - Branch for X Axis Total Quantity for Y Axis
        plt.bar(result['Branch'], result['Quantity'], width=0.6,color=['purple','blue', 'yellow']) 
        plt.xlabel("Branches")
        plt.ylabel("Sales")
        plt.title("Sales Analysis By Branch")
        plt.show()


# Weekly Analysis - Analysis for given week
class WeeklyAnalysis(Analysis):
    def performAnalysis(self):
        # Load data set into panda frame
        df = pd.read_csv('C:/Users/USER/AppData/Local/Programs/Python/Python313/supermarket.csv')
        
        # Input first day of the week
        day1 = int(input("Enter starting day of the week = "))
        # Filter data for 7 days starting from input day
        day2 = day1 + 6
        filtered_df = df.loc[(df['Day'] >= day1) & (df['Day'] <= day2)]
        
        # Add up Sales quantities for each branch
        result = filtered_df.groupby('Branch')['Quantity'].sum().reset_index()
        print("Products Summary")
        print(result)  # Display summary result in tabular form
        
        # Draw bar chart - Branches for X axis , Quantities for Y Axis
        plt.bar(result['Branch'], result['Quantity'], width=0.6, color=['purple','blue', 'yellow'])
        plt.xlabel("Branches")
        plt.ylabel("Sales")
        plt.title("Weekly Sales Analysis By Branch")
        plt.show()


# Price Analysis - Analysis by product price
class PriceAnalysis(Analysis):
    def performAnalysis(self):
        # Load data set into panda frame
        df = pd.read_csv('C:/Users/USER/AppData/Local/Programs/Python/Python313/supermarket.csv')
        
        # Input product name
        product = input("Enter Product Name = ")
        # Filter data for given product name
        filtered_df = df.loc[df['Product'] == product]
        x = filtered_df["Day"]  # Day for X axis
        y = filtered_df["Price"]  # Price for Y axis
        
        print(filtered_df)  # Print filtered data
        # Draw Line Chart - Day for X Axis and Price for Y Axis
        plt.plot(x, y, marker='o')
        plt.xlabel("Day")
        plt.ylabel("Price")
        plt.title("Price Analysis of product")
        plt.show()



# Preference Analysis - Sales analysis by preference
class PreferenceAnalysis(Analysis):
    def performAnalysis(self):
        # Load data set into panda frame
        df = pd.read_csv('C:/Users/USER/AppData/Local/Programs/Python/Python313/supermarket.csv')
        
        # Summarize filtered data to find total quantity for each product
        result = df.groupby('Product')['Quantity'].sum().reset_index()
        print(result)  # Print summary

        # Draw Bar Chart - Product for X Axis Total Quantity for Y Axis
        plt.bar(result['Product'], result['Quantity'], width=0.6, color=['purple','blue', 'yellow'])
        plt.xlabel("ProductS")
        plt.ylabel("Sales")
        plt.title("Sales Analysis By Product")
        plt.show()



# Distribution Analysis - Analysis of products distribution
class DistributionAnalysis(Analysis):
    def performAnalysis(self):
        # Load data set into panda frame
        df = pd.read_csv('C:/Users/USER/AppData/Local/Programs/Python/Python313/supermarket.csv')
        
        result = df.groupby('Branch')['Quantity'].sum().reset_index()
        print(result)

        # Pie chart
        plt.pie(result['Quantity'], labels=result['Branch'], autopct='%1.1f%%', startangle=90, colors=['purple','blue', 'yellow'])
        plt.title("Sales Analysis By Branch")
        plt.axis('equal')
        plt.show()





# Strategy Pattern - Executes the strategy
class ProcessStrategy:
    def executeStrategy(self, analysis_object):
        analysis_object.performAnalysis()


# Strategy Selector - Menu to select analysis strategy
class StrategySelector:
    def openMenu(self):
        while True:
            # Display menu options
            print("Sampath Food City (PVT) Ltd - Registration Analysis")
            print("1 - Analysis By Branch")
            print("2 - Weekly Analysis")
            print("3 - Price Analysis of Product")
            print("4 - Product Preference Analysis")
            print("5 - Distribution Analysis")
            print("6 - Exit")

            # Input user choice
            try:
                choice = int(input("Enter Choice 1 | 2 | 3 | 4 | 5 | 6 = "))
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 6.")
                continue

            # Execute corresponding analysis strategy
            ps = ProcessStrategy()
            if choice == 1:
                branchAnalysisObj = BranchAnalysis()
                ps.executeStrategy(branchAnalysisObj)
            elif choice == 2:
                weeklyAnalysisObj = WeeklyAnalysis()
                ps.executeStrategy(weeklyAnalysisObj)
            elif choice == 3:
                priceAnalysisObj = PriceAnalysis()
                ps.executeStrategy(priceAnalysisObj)
            elif choice == 4:
                preferenceAnalysisObj = PreferenceAnalysis()
                ps.executeStrategy(preferenceAnalysisObj)
            elif choice == 5:
                distributionAnalysisObj = DistributionAnalysis()
                ps.executeStrategy(distributionAnalysisObj)
            elif choice == 6:
                break
            else:
                print("Invalid Choice")

        print("******** END *********")


# Admin Class - Single Admin User
class Admin:
    count = 0

    def __init__(self, username, password):
        # Allow only one Admin instance
        if Admin.count == 0:
            self.username = username
            self.password = password
            Admin.count += 1
        else:
            print("Admin already exists")

    def logon(self):
        # Input user credentials
        print("Sampath Food City (PVT) Ltd")
        user_name = input("User Name = ")
        password = input("Password = ")
        # Verify credentials
        if user_name == self.username and password == self.password:
            s1 = StrategySelector()
            s1.openMenu()
        else:
            print("Incorrect User Name OR Password. Try Again")


# Main Program
a1 = Admin("Admin", "Admin@123")  # Initialize Admin user
a1.logon()  # Log in Admin user

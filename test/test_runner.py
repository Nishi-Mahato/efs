from unittest import TestLoader, TestSuite, TextTestRunner
from Login_test import LoginTest
from stock_edit import StockEditTest
from Stock_add import StockAddTest
from stock_delete import StockDeleteTest
from investment_add import InvestmentAddTest
from investment_edit import InvestmentEditTest
from investment_delete import InvestmentDeleteTest
from cust_edit import CustEditTest
from cust_delete import CustDeleteTest
from cust_summary import CustSummaryTest


if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((

        loader.loadTestsFromTestCase(LoginTest),
        loader.loadTestsFromTestCase(StockAddTest),
        loader.loadTestsFromTestCase(StockEditTest),
        loader.loadTestsFromTestCase(StockDeleteTest),
        loader.loadTestsFromTestCase(InvestmentAddTest),
        loader.loadTestsFromTestCase(InvestmentEditTest),
        loader.loadTestsFromTestCase(InvestmentDeleteTest),
        loader.loadTestsFromTestCase(CustEditTest),
        loader.loadTestsFromTestCase(CustDeleteTest),
        loader.loadTestsFromTestCase(CustSummaryTest),
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
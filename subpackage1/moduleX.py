# import pathlib
# currentFolderPath = pathlib.Path(__file__).parent.resolve()
# print("------------")
# print(currentFolderPath)
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
# https://medium.com/pyladies-taiwan/python-%E7%9A%84-import-%E9%99%B7%E9%98%B1-3538e74f57e3

# 測試 下面的 方法看看
# https://www.geeksforgeeks.org/python-import-from-parent-directory/

# todo https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
import sys
print(sys.version)
print(sys.version_info)
print(sys.path)
# todo 在 webcrawler 試試看

# from .moduleY import sample
# 這種情況 
# python3 -m subpackage1.moduleX
# 可以成功


# from moduleY import sample
# 這種方法可以 是因為 假設 moduleY 是全局維一的變數 
# 如果這個 名稱並非維一   將會有問題
# 或是如果 專案結構更加複雜 需要加上 package directory
from moduleY import sample
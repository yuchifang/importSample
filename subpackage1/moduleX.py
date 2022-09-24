# from .moduleY import sample
# 這種情況 
# python3 -m subpackage1.moduleX
# python -m subpackage1.moduleX
# todo 將 importSample 當作執行環境
# 可以成功
# from .moduleY import sample
# from subpackage1.moduleY import sample

# A absolute import
# R relative import
# todo moduleY
# A
# from . import moduleY
# R
# from . import moduleY
# todo moduleZ
# import subpackage2.moduleZ
# from subpackage2 import moduleZ
# todo moduleA
# from moduleA import sample



# from moduleY import sample
# 這種方法可以 是因為 假設 moduleY 是全局維一的變數 
# 如果這個 名稱並非維一   將會有問題
# 或是如果 專案結構更加複雜 需要加上 package directory

# sample()
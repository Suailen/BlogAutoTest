from common.Utils import BlogDriver
from tests import BlogLogin, BlogList, BlogDetail, BlogEdit, BlogUpdate

if __name__=="__main__":
    #未登录成功
    BlogLogin.BlogLogin().LoginFail()
    #登录成功
    BlogLogin.BlogLogin().LoginSuc()
    #登录状态
    #博客列表页面测试
    BlogList.BlogList().ListTestByLogin()
    #博客详情页面测试
    BlogDetail.BlogDetail().DetailTestByLogin()
    #博客编辑页面测试
    BlogEdit.BlogEdit().EditTestByLogin()
    #发布成功
    BlogEdit.BlogEdit().SubmitSuc()
    #发布失败
    BlogEdit.BlogEdit().SubmitFail()
    #博客更新页面测试
    BlogUpdate.BlogUpdate().UpdateTestByLogin()
    #博客更新成功
    BlogUpdate.BlogUpdate().BlogUpdateSuc()
    #博客更新失败
    BlogUpdate.BlogUpdate().BlogUpdateFail()
    #未登录状态
    BlogList.BlogList().ListTestByNotLogin()
    BlogDetail.BlogDetail().DetailTestByNotLogin()
    BlogEdit.BlogEdit().EditTestByNotLogin()
    BlogUpdate.BlogUpdate().UpdateTestByNotLogin()
    #浏览器退出
    BlogDriver.driver.quit()
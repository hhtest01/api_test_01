
import unittest

from loguru import logger

from api.user_manager import UserManager
from data.user_manager_data import UserManagerData
class TestUserManager(unittest.TestCase):
    user_id = 0

    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManager()
        cls.username = UserManagerData.add_user_data.get("username")
        cls.new_username = UserManagerData.add_user_data.get("new_user_name")
        cls.password = UserManagerData.add_user_data.get("password")

    #case1:添加管理员：只输入用户名密码的情况
    def test01_add_user(self):
        # self.username = "lhuan08"
        # self.password = "123456"
        self.user.id = None
        actul_result = self.user.add_user(self.username, self.password)
        data = actul_result.get("data")
        if data:
            self.user_id = data.get("id")
            TestUserManager.user_id = self.user_id
        self.assertEqual(0,actul_result["errno"])
        self.assertEqual(self.username,actul_result.get("data").get("username"))
    # case2:编辑用户：修改的是用户名名称
    def test02_edit_username(self):
        actual_result = self.user.edit_user(TestUserManager.user_id,self.new_username,password=123456)
        self.assertEqual(0, actual_result["errno"])
        self.assertEqual(self.new_username, actual_result.get("data").get("username"))
    # case3：查询用户列表
    def test03_search_user(self):

        actual_result = self.user.search_user()
        logger.info("查询结果:{}".format(actual_result))
        #self.assertEqual(0, actual_result["errno"])
        # self.assertEqual(self.new_username, actual_result.get("data").get("username"))



    # case1:删除指定id的用户名
    def test04_delete_user(self):
        actual_result = self.user.delete_user(TestUserManager.user_id,self.new_username)
        self.assertEqual(0,actual_result["errno"])




if __name__ == '__main__':
    unittest.main()
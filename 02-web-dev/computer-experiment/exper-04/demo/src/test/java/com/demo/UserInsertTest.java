package com.demo;

import com.demo.entity.User;
import com.demo.mapper.UserMapper;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
/**
 * 用户插入数据单元测试类
 */
@SpringBootTest
public class UserInsertTest {

    @Autowired
    private UserMapper userMapper;

    @Test
    public void testInsertByMapper() {
        User user = new User();
        user.setName("张三丰");
        user.setAge(100);
        user.setGender(1);
        user.setPhone("18800000006");
        int rows = userMapper.insert(user);
        System.out.println("rows: " + rows);
        System.out.println("当前数据库全部用户");
        userMapper.findAll().forEach(System.out::println);
    }
}

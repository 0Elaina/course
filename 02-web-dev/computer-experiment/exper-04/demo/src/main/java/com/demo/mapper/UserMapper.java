package com.demo.mapper;

import com.demo.entity.User;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Options;
import org.apache.ibatis.annotations.Select;

import java.util.List;

/**
 * 用户持久层接口
 */
@Mapper
public interface UserMapper {

    /**
     * 查询所有用户列表
     */
    @Select("SELECT id, name, age, gender, phone FROM user")
    List<User> findAll();

    /**
     * 根据 ID 查询单个用户
     */
    @Select("SELECT id, name, age, gender, phone FROM user WHERE id = #{id}")
    User findById(Integer id);

    @Options(keyProperty = "id", useGeneratedKeys = true)
    @Insert("insert into user(name, age, gender, phone) "
            + "values(#{name}, #{age}, #{gender}, #{phone})")
    int insert(User user);
}

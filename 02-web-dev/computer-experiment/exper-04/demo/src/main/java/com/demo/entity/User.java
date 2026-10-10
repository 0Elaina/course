package com.demo.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * 用户实体类
 * 映射数据库中的 user 表
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    /**
     * ID 主键，自增
     */
    private Integer id;

    /**
     * 姓名
     */
    private String name;

    /**
     * 年龄
     */
    private Integer age;

    /**
     * 性别, 1:男, 2:女
     */
    private Integer gender;

    /**
     * 手机号
     */
    private String phone;
}

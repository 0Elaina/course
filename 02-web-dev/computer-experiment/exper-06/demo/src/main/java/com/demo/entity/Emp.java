package com.demo.entity;

import java.time.LocalDate;
import java.time.LocalDateTime;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * 员工实体类
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Emp {
    /** ID */
    private Integer id;
    /** 用户名 */
    private String username;
    /** 密码 */
    private String password;
    /** 姓名 */
    private String name;
    /** 性别: 1 男, 2 女 */
    private Short gender;
    /** 图像 URL */
    private String image;
    /** 职位: 1 班主任, 2 讲师, 3 学工主管, 4 教研主管 */
    private Short job;
    /** 入职时间（与数据库 entrydate 字段对应） */
    private LocalDate entrydate;
    /** 部门ID（与数据库 dept_id 字段对应） */
    private Integer deptId;
    /** 创建时间 */
    private LocalDateTime createTime;
    /** 修改时间 */
    private LocalDateTime updateTime;

    /**
     * 兼容驼峰命名的获取方式
     */
    public LocalDate getEntryDate() {
        return this.entrydate;
    }

    /**
     * 兼容驼峰命名的设置方式
     */
    public void setEntryDate(LocalDate entryDate) {
        this.entrydate = entryDate;
    }
}

package com.demo.entity;

import java.time.LocalDateTime;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * 部门实体类
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Dept {
    /** 主键ID */
    private Integer id;
    /** 部门名称 */
    private String name;
    /** 创建时间 */
    private LocalDateTime createTime;
    /** 修改时间 */
    private LocalDateTime updateTime;
}

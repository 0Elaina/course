package com.demo.mapper;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import com.demo.entity.Dept;

@Mapper
public interface DeptMapper {
    @Update("update tb_dept set name = #{name}, update_time = #{updateTime} where id = #{id}")
    int update(Dept dept);

    @Select("select * from tb_dept where id = #{id}")
    Dept selectById(@Param("id") Integer id);
}

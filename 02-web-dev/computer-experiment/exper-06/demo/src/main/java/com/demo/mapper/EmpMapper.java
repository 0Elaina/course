package com.demo.mapper;

import java.time.LocalDate;
import java.util.List;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import com.demo.entity.Emp;

@Mapper
public interface EmpMapper {
    void insert(Emp emp);

    int update(Emp emp);

    @Delete("DELETE FROM tb_emp WHERE id = #{id}")
    int deleteById(@Param("id") Integer id);

    List<Emp> list(
            @Param("name") String name,
            @Param("gender") Short gender,
            @Param("begin") LocalDate begin,
            @Param("end") LocalDate end);
}

package com.demo.service;

import java.time.LocalDateTime;
import java.util.List;

import org.springframework.beans.BeanUtils;
import org.springframework.stereotype.Service;

import com.demo.dto.PageEmp;
import com.demo.dto.PageResult;
import com.demo.entity.Emp;
import com.demo.mapper.EmpMapper;
import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class EmpService {
    private final EmpMapper empMapper;

    public void save(Emp emp) {
        emp.setCreateTime(LocalDateTime.now());
        emp.setUpdateTime(LocalDateTime.now());
        empMapper.insert(emp);
    }

    public void update(Emp emp) {
        Emp newEmp = new Emp();
        BeanUtils.copyProperties(emp, newEmp);
        newEmp.setUpdateTime(LocalDateTime.now());
        empMapper.update(newEmp);
    }

    public void deleteById(Integer id) {
        empMapper.deleteById(id);
    }

    public PageResult<Emp> list(
            PageEmp pageEmp) {
        PageHelper.startPage(pageEmp.getPageNum(), pageEmp.getPageSize());

        List<Emp> empList = empMapper.list(
                pageEmp.getName(),
                pageEmp.getGender(),
                pageEmp.getBegin(),
                pageEmp.getEnd());

        PageInfo<Emp> info = new PageInfo<>(empList);
        long total = info.getTotal();
        List<Emp> rows = info.getList();

        return new PageResult<>(total, rows);
    }
}

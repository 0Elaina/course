package com.demo.service;

import java.time.LocalDateTime;

import org.springframework.stereotype.Service;

import com.demo.entity.Dept;
import com.demo.mapper.DeptMapper;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class DeptService {
    private final DeptMapper deptMapper;

    public Dept getById(Integer id) {
        return deptMapper.selectById(id);
    }

    public void update(Dept dept) {
        Dept existDept = deptMapper.selectById(dept.getId());
        existDept.setName(dept.getName());
        existDept.setUpdateTime(LocalDateTime.now());
        deptMapper.update(existDept);
    }
}

-- 1. 保证重复启动可执行（先删从表，再删主表）
drop table if exists tb_emp;
drop table if exists tb_dept;

-- 2. 部门管理
create table tb_dept(
    id int primary key auto_increment comment '主键ID',
    name varchar(10) not null unique comment '部门名称',
    create_time timestamp not null comment '创建时间',
    update_time timestamp not null comment '修改时间'
);

-- 3. 员工管理(带约束)
create table tb_emp (
    id int primary key auto_increment comment 'ID',
    username varchar(20) not null unique comment '用户名',
    password varchar(32) default '123456' comment '密码',
    name varchar(10) not null comment '姓名',
    gender tinyint not null comment '性别, 说明: 1 男, 2 女',
    image varchar(300) comment '图像',
    job tinyint comment '职位, 说明: 1 班主任, 2 讲师, 3 学工主管, 4 教研主管',
    entrydate date comment '入职时间',
    dept_id int comment '部门ID',
    create_time timestamp not null comment '创建时间',
    update_time timestamp not null comment '修改时间'
);

-- 4. 表级注释（H2 标准语法）
comment on table tb_dept is '部门表';
comment on table tb_emp is '员工表';
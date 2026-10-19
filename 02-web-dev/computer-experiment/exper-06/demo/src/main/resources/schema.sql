-- 部门管理表（仅在不存在时创建）
create table if not exists tb_dept (
    id int primary key auto_increment comment '主键ID',
    name varchar(10) not null unique comment '部门名称',
    create_time timestamp not null comment '创建时间',
    update_time timestamp not null comment '修改时间'
);
comment on table tb_dept is '部门表';

-- 员工管理表（仅在不存在时创建）
create table if not exists tb_emp (
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
comment on table tb_emp is '员工表';

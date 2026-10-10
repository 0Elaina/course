-- 如果已存在 user 表则先删除，确保项目启动时幂等初始化
DROP TABLE IF EXISTS user;

-- 用户表
CREATE TABLE user (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT COMMENT 'ID',
    name VARCHAR(100) COMMENT '姓名',
    age TINYINT UNSIGNED COMMENT '年龄',
    gender TINYINT UNSIGNED COMMENT '性别, 1:男, 2:女',
    phone VARCHAR(11) COMMENT '手机号'
) COMMENT '用户表' ENGINE=InnoDB DEFAULT CHARSET=utf8;

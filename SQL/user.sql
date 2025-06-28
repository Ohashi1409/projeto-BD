CREATE TABLE user_table (
    id VARCHAR(100) PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    rating VARCHAR(255),
    password VARCHAR(255) NOT NULL,
    user_city VARCHAR(255),
    user_country VARCHAR(255),
    user_state VARCHAR(255),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE friendship (
    id_1 VARCHAR(100),
    id_2 VARCHAR(100),
    PRIMARY KEY (id_1, id_2),
    FOREIGN KEY (id_1) REFERENCES user_table(id),
    FOREIGN KEY (id_2) REFERENCES user_table(id)
);

CREATE TABLE blog_entry (
    entry_id INTEGER PRIMARY KEY,
    user_id VARCHAR(100) NOT NULL,
    title VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES user_table(id)
);

CREATE TABLE blog_comment (
    comment_id INTEGER PRIMARY KEY,
    comment_id_pai INTEGER,
    FOREIGN KEY (comment_id_pai) REFERENCES blog_comment(comment_id)
);

CREATE TABLE blog_entry_comment (
    blog_entry_id INTEGER,
    comment_id INTEGER,
    user_id VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (blog_entry_id, comment_id, user_id, created_at),
    FOREIGN KEY (blog_entry_id) REFERENCES blog_entry(entry_id),
    FOREIGN KEY (comment_id) REFERENCES blog_comment(comment_id),
    FOREIGN KEY (user_id) REFERENCES user_table(id)
);

CREATE TABLE group_table (
    group_id INTEGER PRIMARY KEY,
    user_id_creator VARCHAR(100) NOT NULL,
    group_name VARCHAR(255),
    group_type VARCHAR(255),
    is_private NUMBER(1) DEFAULT 1,
    FOREIGN KEY (user_id_creator) REFERENCES user_table(id)
);


CREATE TABLE user_participates_group (
    group_id INTEGER,
    user_id VARCHAR(100),
    PRIMARY KEY (group_id, user_id),
    FOREIGN KEY (group_id) REFERENCES group_table(group_id),
    FOREIGN KEY (user_id) REFERENCES user_table(id)
);

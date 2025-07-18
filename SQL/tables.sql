USE `codeforces-db`;

CREATE TABLE user_table (
    id VARCHAR(100) PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    rating INT,
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
    entry_id INT PRIMARY KEY,
    user_id VARCHAR(100) NOT NULL,
    title VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES user_table(id)
);

CREATE TABLE blog_comment (
    comment_id INT PRIMARY KEY,
    comment_id_pai INT,
    FOREIGN KEY (comment_id_pai) REFERENCES blog_comment(comment_id)
);

CREATE TABLE blog_entry_comment (
    blog_entry_id INT,
    comment_id INT,
    user_id VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (blog_entry_id, comment_id, user_id, created_at),
    FOREIGN KEY (blog_entry_id) REFERENCES blog_entry(entry_id),
    FOREIGN KEY (comment_id) REFERENCES blog_comment(comment_id),
    FOREIGN KEY (user_id) REFERENCES user_table(id)
);

CREATE TABLE group_table (
    group_id INT PRIMARY KEY,
    user_id_creator VARCHAR(100) NOT NULL,
    group_name VARCHAR(255),
    group_type VARCHAR(255),
    is_private TINYINT(1) DEFAULT 1,
    FOREIGN KEY (user_id_creator) REFERENCES user_table(id)
);

CREATE TABLE user_participates_group (
    group_id INT,
    user_id VARCHAR(100),
    PRIMARY KEY (group_id, user_id),
    FOREIGN KEY (group_id) REFERENCES group_table(group_id),
    FOREIGN KEY (user_id) REFERENCES user_table(id)
);

CREATE TABLE contest_table (
    contest_id INT PRIMARY KEY,
    group_id INT,
    user_id_creator VARCHAR(100),
    is_private TINYINT(1) DEFAULT 1,
    startTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    frozen_contest TINYINT(1) DEFAULT 0,
    contest_duration TIME,
    contest_name VARCHAR(255),
    FOREIGN KEY (group_id) REFERENCES group_table(group_id),
    FOREIGN KEY (user_id_creator) REFERENCES user_table(id)
);

CREATE TABLE gym_table (
    contest_id INT,
    institution VARCHAR(255),
    original_event_name VARCHAR(255),
    PRIMARY KEY (contest_id),
    FOREIGN KEY (contest_id) REFERENCES contest_table(contest_id)
);

CREATE TABLE user_participates_contest (
    user_id VARCHAR(100),
    contest_id INT,
    ranking INT,
    PRIMARY KEY (user_id, contest_id),
    FOREIGN KEY (user_id) REFERENCES user_table(id),
    FOREIGN KEY (contest_id) REFERENCES contest_table(contest_id)
);

CREATE TABLE problem_table (
    problem_id INT PRIMARY KEY,
    problem_statement VARCHAR(500),
    difficulty VARCHAR(100),
    problem_index INT,
    points INT DEFAULT 0,
    solved_count INT DEFAULT 0
);

CREATE TABLE problem_supported_languages (
    problem_id INT,
    supported_language VARCHAR(255),
    PRIMARY KEY (problem_id, supported_language),
    FOREIGN KEY (problem_id) REFERENCES problem_table(problem_id)
);

CREATE TABLE submission_table (
    submission_id INT PRIMARY KEY,
    problem_id INT NOT NULL,
    user_id VARCHAR(100) NOT NULL,
    submission_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    submission_language VARCHAR(255),
    time_consumed TIME,
    points INT,
    FOREIGN KEY (user_id) REFERENCES user_table(id),
    FOREIGN KEY (problem_id) REFERENCES problem_table(problem_id)
);

CREATE TABLE verdict_table (
    verdict_id INT PRIMARY KEY
);

CREATE TABLE submission_problem (
    submission_id INT,
    problem_id INT,
    verdict_id INT,
    status_submission_problem VARCHAR(100),
    PRIMARY KEY (submission_id, problem_id),
    FOREIGN KEY (submission_id) REFERENCES submission_table(submission_id),
    FOREIGN KEY (problem_id) REFERENCES problem_table(problem_id),
    FOREIGN KEY (verdict_id) REFERENCES verdict_table(verdict_id)
);

CREATE TABLE contest_fazParte (
    contest_id INT,
    submission_id INT,
    problem_id INT,
    PRIMARY KEY (contest_id, submission_id, problem_id),
    FOREIGN KEY (contest_id) REFERENCES contest_table(contest_id),
    FOREIGN KEY (submission_id, problem_id) REFERENCES submission_problem(submission_id, problem_id)
);

CREATE TABLE test_case (
    test_case_disc VARCHAR(255),
    problem_id INT,
    PRIMARY KEY (problem_id, test_case_disc),
    FOREIGN KEY (problem_id) REFERENCES problem_table(problem_id)
);

CREATE TABLE solution (
    problem_id INT,
    PRIMARY KEY (problem_id),
    FOREIGN KEY (problem_id) REFERENCES problem_table(problem_id)
);
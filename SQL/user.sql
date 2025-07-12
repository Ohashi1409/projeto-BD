CREATE TABLE user_table (
    id VARCHAR(100) PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    rating INTEGER,
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

CREATE TABLE contest_table (
    contest_id INTEGER,
    group_id INTEGER,
    user_id_creator VARCHAR(100),
    is_private NUMBER(1) DEFAULT 1,
    startTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    frozen_contest NUMBER(1) DEFAULT 0,
    -- Precisa codar pra organizar o duration
    contest_duration INTERVAL DAY(3) TO SECOND(2),
    contest_name VARCHAR(255),
    PRIMARY KEY (contest_id),
    FOREIGN KEY (group_id) REFERENCES group_table(group_id),
    FOREIGN KEY (user_id_creator) REFERENCES user_table(id)
);

CREATE TABLE gym_table (
    contest_id INTEGER,
    institution VARCHAR(255),
    original_event_name VARCHAR(255),
    PRIMARY KEY (contest_id),
    FOREIGN KEY (contest_id) REFERENCES contest_table(contest_id)
);

CREATE TABLE user_participates_contest (
    user_id VARCHAR(100),
    contest_id INTEGER,
    -- Codar ranking, pois ele é um atributo derivado 
    ranking INTEGER,
    PRIMARY KEY (user_id, contest_id),
    FOREIGN KEY (user_id) REFERENCES user_table(id),
    FOREIGN KEY (contest_id) REFERENCES contest_table(contest_id)
);

CREATE TABLE problem_table (
    problem_id INTEGER,
    difficulty VARCHAR(100),
    problem_index INTEGER,
    points INTEGER DEFAULT 0,
    solved_count INTEGER DEFAULT 0,
    PRIMARY KEY (problem_id)
);

CREATE TABLE problem_supported_languages (
    problem_id INTEGER,
    language VARCHAR(255),
    PRIMARY KEY (problem_id, language),
    FOREIGN KEY (problem_id) REFERENCES problem_table(problem_id)
);

CREATE TABLE submission_table (
    submission_id INTEGER,
    problem_id INTEGER NOT NULL,
    user_id VARCHAR(100) NOT NULL,
    submission_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    submission_language VARCHAR(255),
    -- Codar pra organizar o tempo
    time_consumed INTERVAL DAY(3) TO SECOND(2),
    points INTEGER,
    PRIMARY KEY (submission_id),
    FOREIGN KEY (user_id) REFERENCES user_table(id),
    FOREIGN KEY (problem_id) REFERENCES problem_table(problem_id)
);

CREATE TABLE verdict_table (
    verdict_id INTEGER,
    PRIMARY KEY (verdict_id)
);

CREATE TABLE submission_problem (
    submission_id INTEGER,
    problem_id INTEGER,
    verdict_id INTEGER,
    status_submission_problem VARCHAR(100),
    PRIMARY KEY (submission_id, problem_id),
    FOREIGN KEY (submission_id) REFERENCES submission_table(submission_id),
    FOREIGN KEY (problem_id) REFERENCES problem_table(problem_id),
    FOREIGN KEY (verdict_id) REFERENCES verdict_table(verdict_id)
);

CREATE TABLE contest_fazParte (
    contest_id INTEGER,
    submission_id INTEGER,
    problem_id INTEGER,
    PRIMARY KEY (contest_id, submission_id, problem_id),
    FOREIGN KEY (contest_id) REFERENCES contest_table(contest_id),
    FOREIGN KEY (submission_id) REFERENCES submission_problem(submission_id),
    FOREIGN KEY (problem_id) REFERENCES submission_problem(problem_id)
);

CREATE TABLE test_case (
    test_case_disc VARCHAR(255),
    problem_id INTEGER,
    PRIMARY KEY (problem_id, test_case_disc),
    FOREIGN KEY (problem_id) REFERENCES problem_table(problem_id)
);

CREATE TABLE solution (
    problem_id INTEGER,
    PRIMARY KEY (problem_id)
);
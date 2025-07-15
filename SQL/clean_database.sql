-- Script para limpar o banco de dados MySQL

USE `codeforces-db`;

-- Desabilita verificação de chaves estrangeiras temporariamente
SET FOREIGN_KEY_CHECKS = 0;

-- Limpa tabelas na ordem correta (filhas primeiro, pais depois)
DELETE FROM contest_fazParte;
DELETE FROM submission_problem;
DELETE FROM submission_table;
DELETE FROM user_participates_contest;
DELETE FROM gym_table;
DELETE FROM contest_table;
DELETE FROM user_participates_group;
DELETE FROM group_table;
DELETE FROM problem_supported_languages;
DELETE FROM test_case;
DELETE FROM solution;
DELETE FROM problem_table;
DELETE FROM verdict_table;
DELETE FROM blog_entry_comment;
DELETE FROM blog_comment;
DELETE FROM blog_entry;
DELETE FROM friendship;
DELETE FROM user_table;

SET FOREIGN_KEY_CHECKS = 1;

SELECT 'Banco de dados limpo com sucesso!' as status;
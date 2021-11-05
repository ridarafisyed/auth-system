CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `f_name` varchar(255),
  `l_name` varchar(255),
  `m_name` varchar(255),
  `company` int,
  `uname` varchar(255),
  `pword` varchar(255),
  `created_at` timestamp,
  `country_code` int
);

CREATE TABLE `profiles` (
  `p_id` int PRIMARY KEY AUTO_INCREMENT,
  `emp_pers_email` varchar(255),
  `user_dob` datetime,
  `emp_ssn` int,
  `user` int,
  `job_title` varchar(255),
  `bar_no` int,
  `role` varchar(255),
  `group` varchar(255),
  `timezone` timezone,
  `rate` float,
  `company_email` varchar(255),
  `round_enteries` int,
  `add_street` varchar(255),
  `add_suite` varchar(255),
  `add_city` varchar(255),
  `add_state` varchar(255),
  `add_zip` varchar(255),
  `mob_no` int,
  `work_no` int,
  `home_no` int,
  `extention` int,
  `alt_email` varchar(255),
  `fbook` varchar(255),
  `linkedin` varchar(255),
  `other_media` varchar(255),
  `twitter` varchar(255),
  `website` varchar(255),
  `client_email` varchar(255),
  `n_prefix` varchar(255),
  `n_suffix` varchar(255),
  `PhoneExt` int,
  `avatar` varchar(255)
);

CREATE TABLE `users_bill_info` (
  `id` int,
  `user_id` int,
  `cc_fname` varchar(255),
  `cc_lname` varchar(255),
  `bank_name` varchar(255),
  `routing` int,
  `bnk_acc_no` varchar(255),
  `credit_card` int,
  `security_id` int,
  `expriation` datetime,
  `acc_pay_em_in` varchar(255),
  `acc_pay_em_out` varchar(255),
  `bill_add_street` varchar(255),
  `bill_add_suite` varchar(255),
  `bill_add_city` varchar(255),
  `bill_add_county` varchar(255),
  `bill_add_state` varchar(255),
  `bill_add_zip` varchar(255),
  `bill_add_ext` varchar(255),
  `bill_type` varchar(255),
  `bill_date` datetime
);

CREATE TABLE `debtors` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `jdg_type` varchar(255),
  `jdg_date` datetime,
  `dbt_fname` varchar(255),
  `dbt_lname` varchar(255),
  `dbt_hair` varchar(255),
  `dbt_height` int,
  `dbt_mname` varchar(255),
  `dbt_phone` int,
  `dbt_gender` varchar(255),
  `dbt_bod` date,
  `dbt_ethnicity` varchar(255),
  `dbt_eye` varchar(255),
  `dbt_skill` varchar(255),
  `dbt_ssn` int,
  `dbt_weight` int,
  `dbt_4` int,
  `dbt_add` varchar(255),
  `dbt_bank` varchar(255),
  `dbt_unit` varchar(255),
  `dbt_city` varchar(255),
  `dbt_county` varchar(255),
  `dbt_state` varchar(255),
  `dbt_zip` int,
  `dbt_license_no` varchar(255),
  `dbt_license` varchar(255),
  `dbt_emp_4` int,
  `dbt_emp_add` varchar(255),
  `dbt_emp_city` varchar(255),
  `dbt_emp_state` varchar(255),
  `dbt_emp_unit` varchar(255),
  `dbt_emp_zip` int,
  `dbt_emp_website` varchar(255),
  `dbt_emp_county` varchar(255),
  `dbt_emp_email` varchar(255),
  `dbt_emp_phone` int
);

CREATE TABLE `invoices` (
  `inv_id` int PRIMARY KEY AUTO_INCREMENT,
  `inv_client_id` int,
  `inv_date_issued` date,
  `inv_date_payed` date,
  `inv_client_name` varchar(255),
  `inv_disputed` varchar(255),
  `inv_date_due` date,
  `inv_interest_due` date,
  `inv_status` varchar(255),
  `inv_matter_id` int,
  `inv_note` varchar(255),
  `inv_date_period` date,
  `inv_t_and_c` varchar(255),
  `inv_void` varchar(255),
  `inv_amount` float,
  `inv_disc` float,
  `inv_fees` int,
  `inv_misc_fees` int,
  `time_atty` varchar(255),
  `time_paralegal` varchar(255),
  `time_other` varchar(255),
  `trans_type` varchar(255)
);

CREATE TABLE `fee` (
  `cnty_fees` float,
  `court_fees` float,
  `harecost` float,
  `interest` float,
  `invoice_amt` float,
  `invoice_disc` float,
  `inv_fees` float,
  `invoice_paid` varchar(255),
  `inv` varchar(255),
  `jdg_amt` float,
  `inv_misc_fees` float,
  `opt_account` int,
  `pmt_received` int,
  `rate` float,
  `sheriff_fees` float,
  `softcost` float,
  `trust_acc` int
);

CREATE TABLE `leads` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `client_id` int,
  `matter_type` varchar(255),
  `cl_ct_plus_4` int,
  `cl_cnt_add` varchar(255),
  `cl_ct_cty` varchar(255),
  `cl_cont_cnty` varchar(255),
  `cl_con_email` varchar(255),
  `cl_con_fname` varchar(255),
  `cl_con_lname` varchar(255),
  `cl_cnt_phone` int,
  `cl_ct_rship` varchar(255),
  `cl_ct_st` varchar(255),
  `cl_ct_unit` varchar(255),
  `cl_ct_zip` int,
  `cl_dt_event` date,
  `cl_matter_type` varchar(255)
);

CREATE TABLE `cl_vic_info` (
  `id` int,
  `client_id` int,
  `cl_vic_atty_email` varchar(255),
  `cl_vic_plus_4` int,
  `cl_vic_add` varchar(255),
  `cl_vic_cty` varchar(255),
  `cl_vic_cnty` varchar(255),
  `cl_vic_dob` date,
  `cl_vic_fname` varchar(255),
  `cl_vic_gen` varchar(255),
  `cl_vic_lname` varchar(255),
  `cl_vic_st` varchar(255),
  `cl_vic_unit` varchar(255),
  `cl_vic_zip` int,
  `cl_vic_atty` varchar(255),
  `cl_vic_atty_id` int
);

CREATE TABLE `cl_vic_atty` (
  `id` int,
  `client_id` int,
  `cl_vic_atty_id` int PRIMARY KEY AUTO_INCREMENT,
  `cl_vic_atty_plus_4` int,
  `cl_vic_atty_add` varchar(255),
  `cl_vic_atty_cty` varchar(255),
  `cl_vic_atty_cnty` varchar(255),
  `cl_vic_atty_fn` varchar(255),
  `cl_vic_atty_ln` varchar(255),
  `cl_vic_atty_phone` int,
  `cl_vic_atty_st` varchar(255),
  `cl_vic_atty_unit` varchar(255),
  `cl_vic_atty_zip` int
);

CREATE TABLE `countries` (
  `code` int PRIMARY KEY,
  `name` varchar(255),
  `continent_name` varchar(255)
);

CREATE TABLE `companies` (
  `cmpy_id` int PRIMARY KEY AUTO_INCREMENT,
  `cmpy_name` varchar(255),
  `cmpy_email` varchar(255),
  `cmpy_address` varchar(255),
  `cmpy_suite` varchar(255),
  `cmpy_city` varchar(255),
  `cmpy_state` varchar(255),
  `cmpy_zip` varchar(255),
  `cmpy_county` int,
  `cmpy_attorneys` int,
  `cmpy_emp` int,
  `cmpy_office` int
);

CREATE TABLE `offices` (
  `office_id` int PRIMARY KEY AUTO_INCREMENT,
  `commpany` int,
  `off_name` varchar(255),
  `off_rep_id` int,
  `off_add` varchar(255),
  `off_add_suite` varchar(255),
  `off_add_city` varchar(255),
  `off_add_state` varchar(255),
  `off_add_zip` varchar(255),
  `off_add_country` int,
  `off_contact_mobile` int,
  `off_contact_home` int,
  `off_contact_work` int,
  `off_fax` int,
  `off_email1` varchar(255),
  `off_email2` varchar(255),
  `off_email3` varchar(255),
  `off_ssn` int
);

CREATE TABLE `job_board` (
  `user_id` int,
  `act_srch` boolean,
  `bar_pass_date` date,
  `gpa` int,
  `grad_date` date,
  `lschool` varchar(255),
  `lic_st` varchar(255),
  `pass_srch` boolean,
  `salary` int,
  `ug_degree` varchar(255),
  `ug_school` varchar(255),
  `relocate` boolean
);

CREATE TABLE `county_recorder` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `cnty_plus_4` int,
  `cnty_add` varchar(255),
  `cnty_city` varchar(255),
  `cnty_email` varchar(255),
  `cnty_phone` int,
  `cnty_state` varchar(255),
  `cnty_suite` varchar(255),
  `cnty_website` varchar(255),
  `cnty_zip` varchar(255)
);

CREATE TABLE `court_records` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `court_plus_4` int,
  `court_add` varchar(255),
  `court_cnty` varchar(255),
  `court_email` varchar(255),
  `court_house_name` varchar(255),
  `court_phone_no` int,
  `court_room` varchar(255),
  `court_state` varchar(255),
  `court_type` varchar(255),
  `court_website` varchar(255),
  `court_zip` int,
  `court_efile_id` int,
  `proc_server_id` int,
  `sheriff_id` int
);

CREATE TABLE `efile_serveices` (
  `court_efile_id` int PRIMARY KEY AUTO_INCREMENT,
  `court_efile_plus_4` int,
  `court_efile_add` varchar(255),
  `court_efile_city` varchar(255),
  `court_efile_unit` varchar(255),
  `court_efile_county` varchar(255),
  `court_efile_state` varchar(255),
  `court_efile_zip` varchar(255),
  `court_efile_website` varchar(255),
  `count_efile_phone_no` int,
  `court_efile_email` varchar(255),
  `court_efile_cmpy_name` archar,
  `court_efile_cont_person` varchar(255),
  `court_efile_cust_rating` varchar(255),
  `court_efile_rate_sheet` varchar(255)
);

CREATE TABLE `process_servers` (
  `proc_server_id` int PRIMARY KEY AUTO_INCREMENT,
  `proc_server_plus_4` int,
  `proc_server_add` varchar(255),
  `proc_server_city` varchar(255),
  `proc_server_unit` varchar(255),
  `proc_server_county` varchar(255),
  `proc_server_state` varchar(255),
  `proc_server_zip` varchar(255),
  `proc_server_website` varchar(255),
  `proc_server_phone_no` int,
  `proc_server_email` varchar(255),
  `proc_server_cmpy_name` archar,
  `proc_server_cont_person` varchar(255),
  `proc_server_cust_rating` varchar(255),
  `proc_server_rate_sheet` varchar(255)
);

CREATE TABLE `sheriff_details` (
  `sheriff_id` int PRIMARY KEY AUTO_INCREMENT,
  `sheriff_plus_4` int,
  `sheriff_add` varchar(255),
  `sheriff_city` varchar(255),
  `sheriff_county` varchar(255),
  `sheriff_state` varchar(255),
  `sheriff_unit` varchar(255),
  `sheriff_zip` int,
  `sheriff_email` varchar(255),
  `sheriff_phone_no` varchar(255),
  `sheriff_website` varchar(255)
);

CREATE TABLE `contact` (
  `contact_id` int PRIMARY KEY AUTO_INCREMENT,
  `office_id` int,
  `company_id` int
);

CREATE TABLE `matters` (
  `matter_id` int PRIMARY KEY AUTO_INCREMENT,
  `matter_name` varchar(255),
  `matter_type` varchar(255),
  `matter_source` varchar(255),
  `matter_status` varchar(255),
  `assign_to` int
);

ALTER TABLE `users` ADD FOREIGN KEY (`company`) REFERENCES `companies` (`cmpy_id`);

ALTER TABLE `profiles` ADD FOREIGN KEY (`user`) REFERENCES `users` (`id`);

ALTER TABLE `users_bill_info` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `invoices` ADD FOREIGN KEY (`inv_matter_id`) REFERENCES `matters` (`matter_id`);

ALTER TABLE `leads` ADD FOREIGN KEY (`client_id`) REFERENCES `users` (`id`);

ALTER TABLE `cl_vic_info` ADD FOREIGN KEY (`client_id`) REFERENCES `users` (`id`);

ALTER TABLE `cl_vic_atty` ADD FOREIGN KEY (`client_id`) REFERENCES `users` (`id`);

ALTER TABLE `companies` ADD FOREIGN KEY (`cmpy_county`) REFERENCES `countries` (`code`);

ALTER TABLE `offices` ADD FOREIGN KEY (`commpany`) REFERENCES `companies` (`cmpy_id`);

ALTER TABLE `offices` ADD FOREIGN KEY (`off_rep_id`) REFERENCES `users` (`id`);

ALTER TABLE `offices` ADD FOREIGN KEY (`off_add_country`) REFERENCES `countries` (`code`);

ALTER TABLE `job_board` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `court_records` ADD FOREIGN KEY (`court_efile_id`) REFERENCES `efile_serveices` (`court_efile_id`);

ALTER TABLE `court_records` ADD FOREIGN KEY (`proc_server_id`) REFERENCES `process_servers` (`proc_server_id`);

ALTER TABLE `court_records` ADD FOREIGN KEY (`sheriff_id`) REFERENCES `sheriff_details` (`sheriff_id`);

ALTER TABLE `matters` ADD FOREIGN KEY (`assign_to`) REFERENCES `users` (`id`);

ALTER TABLE `offices` ADD FOREIGN KEY (`office_id`) REFERENCES `contact` (`office_id`);

ALTER TABLE `companies` ADD FOREIGN KEY (`cmpy_id`) REFERENCES `contact` (`company_id`);

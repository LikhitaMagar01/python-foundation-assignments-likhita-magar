-- 1. Display employee_id, monthly_salary, and monthly_salary + 10000 as increased_salary.
select employee_id, monthly_salary, monthly_salary + 10000 as increased_salary from employees;

-- 2. Calculate reduced_salary by subtracting 5000 from monthly_salary.
select employee_id, monthly_salary, monthly_salary -5000 as reduced_salary from employees;

--3. Calculate annual_salary by multiplying monthly_salary by 12.
select employee_id, monthly_salary, monthly_salary * 12 as annual_salary from employees; 

--4. Calculate average_monthly_bonus by dividing annual_bonus by 12.
select employee_id, monthly_salary, annual_bonus / 12 as average_monthly_bonus from employees; 

--5. Display age and age % 2 as remainder.
select employee_id, age, age % 2 as reminder from employees; 

--6. Calculate total_compensation as (monthly_salary * 12) + annual_bonus.
select employee_id, monthly_salary, (monthly_salary * 12) + annual_bonus as total_compensation from employees; 

--7. Find employees whose monthly_salary is greater than 100000.
select * from employees where monthly_salary > 100000; 

--8. Find employees whose age is less than 30.
select * from employees where age < 30;

--9. Find employees with performance_rating greater than or equal to 4.5.
select * from employees where performance_rating >= 4.5; 

--10. Find employees whose years_experience is less than or equal to 5.
select employee_id, years_experience from employees where years_experience <= 5; 

--11. Find employees whose department is equal to IT.
select employee_id, department from employees where department = 'IT';

--12. Find employees whose employment_status is not equal to Active.
	select employee_id, employment_status from employees where employment_status <> 'Active';

--13. Find employees from Kathmandu AND monthly_salary greater than 100000.
select employee_id, city, monthly_salary from employees where city = 'Kathmandu' and monthly_salary > 100000; 

--14. Find employees from Kathmandu OR Pokhara.
select employee_id, city from employees where city in ('Kathmandu', 'Pokhara'); 

--15. Find employees from IT OR Analytics with performance_rating greater than 4.
select employee_id, department, performance_rating from employees where department in ('IT', 'Analytics') and performance_rating > 4;

--16. Find employees who are NOT remote workers.
select employee_id, remote_worker from employees where remote_worker != 'No'; 

--17. Find employees with age below 40 AND years_experience above 5 AND employment_status = Active.
select employee_id, employment_status from employees where age < 40 and years_experience > 5 and employment_status = 'Active'

--18. Find Full-Time employees with salary above 80000 OR performance_rating above 4.5.
select employee_id, employment_type, monthly_salary, performance_rating from employees where employment_type = 'Full-Time' and (monthly_salary > '80000' or performance_rating > 4.5); 

--19. Find employees whose first_name starts with A.
select employee_id, first_name from employees where first_name like 'A%'; 

--20. Find employees whose first_name ends with a.
select employee_id, first_name from employees where first_name like '%a'; 

--21. Find employees whose first_name contains the letter i.
select employee_id, first_name from employees where first_name like '%i%'; 

--22. Find employees whose last_name starts with S.
select employee_id, last_name from employees where last_name like 'S%'; 

--23. Find employees whose job_title contains the word Analyst.
select employee_id, job_title from employees where job_title like '%Analyst%'; 

--24. Find employees whose email ends with @company.com.
select employee_id, email from employees where email like '%@company.com'; 

--25. Find employees working in Kathmandu, Pokhara, or Lalitpur.
select employee_id, city from employees where city in ('Kathmandu', 'Pokhara', 'Lalitpur'); 

--26. Find employees in the IT, Analytics, or Finance departments.
select employee_id, department from employees where department in ('IT', 'Analytics', 'Finance'); 

--27. Find employees with employment_type Full-Time or Contract.
select employee_id, employment_type from employees where employment_type in ('Full-Time', 'Contract'); 

--28. Find employees whose education_level is Bachelor, Master, or PhD.
select employee_id, education_level from employees where education_level in ('Bachelor', 'Master', 'PhD'); 

--29. Find employees aged between 25 and 40.
select employee_id, age from employees where age between 25 and 40; 

--30. Find employees whose monthly_salary is between 80000 and 150000.
select employee_id, monthly_salary from employees where monthly_salary between 80000 and 150000; 

--31. Find employees with performance_rating between 3.5 and 4.5.
select employee_id, performance_rating from employees where performance_rating between 3.5 and 4.5; 

--32. Find employees with years_experience between 3 and 10.
select employee_id, years_experience from employees where years_experience between 3 and 10; 

--33. Find employees who joined between 2020-01-01 and 2024-12-31.
select employee_id, join_date from employees where join_date between '2020-01-01' and '2024-12-31'; 

--34. Find employees whose email is NULL.
select employee_id, email from employees where email is null; 

--35. Find employees whose phone is NULL.
select employee_id, phone from employees where phone is null; 

--36. Find employees whose emergency_contact is NULL.
select employee_id, emergency_contact from employees where emergency_contact is null; 

--37. Find employees whose certification is NULL.
select employee_id, certification from employees where certification is null; 

--38. Find employees whose email is NOT NULL AND phone is NOT NULL.
select employee_id, email, phone from employees where email is not null and phone is not null; 

--39. Find Active employees from Kathmandu or Lalitpur whose salary is between 90000 and 180000.
select employee_id, employment_status, city, monthly_salary from employees where employment_status = 'Active' and city in ('Kathmandu', 'Lalitpur') and monthly_salary between 90000 and 180000;

--40. Find employees in IT or Analytics whose first_name starts with A and performance_rating is at least 4.
select employee_id, department, first_name, performance_rating from employees where department in ('IT', 'Analytics') and first_name like 'A%' and performance_rating >=4; 

--41. Find employees who are not Interns and have completed more than 5 projects.
select employee_id, employment_type, projects_completed from employees where employment_type <> 'Interns' and projects_completed > 5; 

--42. Find employees with NULL certification OR NULL emergency_contact.
select employee_id, certification, emergency_contact from employees where certification is null or emergency_contact  is null; 

--43. Find employees whose job_title contains Manager and whose employment_status is Active.
select employee_id, job_title from employees where job_title like '%Manager%' and employment_status = 'Active'; 

--44. Display employees aged between 30 and 50 who work remotely and have salary above 120000.
select employee_id, age, remote_worker, monthly_salary from employees where age between 30 and 50 and remote_worker = 'Yes' and monthly_salary > 120000; 

--45. Calculate annual_salary and total_compensation for employees in Finance, IT, and Analytics.
select employee_id, monthly_salary * 12 as annual_salary, (monthly_salary * 12) + annual_bonus as total_compensation from employees where department in ('Finance', 'IT', 'Analytics'); 

--46. Find employees whose promotion_eligible = Yes AND performance_category = Excellent.
select employee_id, promotion_eligible, performance_category from employees where promotion_eligible = 'Yes' and performance_category = 'Excellent'; 

--47. Find employees with overtime_hours between 20 and 60 and leave_days_taken less than 15.
select employee_id, overtime_hours, leave_days_taken from employees where overtime_hours between 20 and 60 and leave_days_taken < 15; 

--48. Find employees from cities other than Kathmandu whose first_name contains the letter u.
select employee_id, city, first_name from employees where city != 'Kathmandu' and first_name like '%u%'; 

--49. Find employees with monthly_salary > 100000 OR annual_bonus > 150000.
select employee_id, monthly_salary, annual_bonus from employees where monthly_salary > 100000 or annual_bonus > 150000; 

--50. Display employee_id, employee_code, first_name, department, monthly_salary, and monthly_salary * 12 as annual_salary for Active employees.
select employee_id, employee_code, first_name, department, monthly_salary, monthly_salary * 12 as annual_salary from employees where employment_status = 'Active'; 

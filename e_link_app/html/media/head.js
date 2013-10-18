// JavaScript Document
function show_login()
{
    document.getElementById("login_div").style.display = "";
    document.getElementById("regist_div").style.display = "none";
}
function show_regist()
{
	document.getElementById("regist_div").style.display = "";
    document.getElementById("login_div").style.display = "none";
}
function submit_login()
{
	if(check_login_empty())
	{
		document.getElementById("login_submit").click();
	}
}
function submit_regist()
{
	if(check_regist_empty())
	{
		document.getElementById("regist_submit").click();
	}
}
function check_login_empty()
{
	if(document.getElementById("login_username").value == "")
	{
		alert("用户名不能为空");
		return false;
	}
	if(document.getElementById("login_password").value == "")
	{
		alert("密码不能为空");
		return false;
	}
	return true;
} 
function check_regist_empty()
{
	if(document.getElementById("regist_username").value == "")
	{
		alert("用户名不能为");
		return false;
	}
	if(document.getElementById("regist_password").value == "" || document.getElementById("conform_password").value == "")
	{
		alert("密码不能为空");
		return false;
	}
	if(document.getElementById("email").value == "")
	{
		alert("邮件不能为空");
		return false;
	}
	return true;
}

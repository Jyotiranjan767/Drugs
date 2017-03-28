package com.update.testCases;

import java.awt.AWTException;

import org.testng.annotations.Test;

import com.update.businessClass.AllInUpdate;

public class Login_ {

	AllInUpdate aiu=new AllInUpdate();
	@Test(priority=1)
	public void login__() throws AWTException{
		aiu.login();
	}
	@Test(priority=2)
	public void upload() throws AWTException, InterruptedException{
		aiu.resumeUpload("Autoamtion");
	}
	@Test(priority=3)
	public void logout() throws InterruptedException{
		aiu.logout();
	}
}

package com.update.businessClass;

import org.openqa.selenium.support.PageFactory;

import com.jyoti.theOnlineDrugstore.ExcelLib.Driver;

import monster.update.pageFactory.Login_monster;

public class AllInUpdatesMonster {

	Login_monster lm=PageFactory.initElements(Driver.driver,Login_monster.class);
	
	public void login() throws InterruptedException{
		
		Driver.driver.get("http://www.monsterindia.com/");
		lm.signIn().click();
		lm.userName().sendKeys("jyotiranjan976@gmail.com");
		Thread.sleep(1000);
		lm.password().sendKeys("hritik");
		lm.submit().click();
	}
}

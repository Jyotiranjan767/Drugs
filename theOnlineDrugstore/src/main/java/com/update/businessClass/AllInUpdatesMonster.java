package com.update.businessClass;

import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.KeyEvent;

import org.openqa.selenium.support.PageFactory;

import com.jyoti.theOnlineDrugstore.ExcelLib.CommonClasses;
import com.jyoti.theOnlineDrugstore.ExcelLib.Driver;

import monster.update.pageFactory.Login_monster;
import monster.update.pageFactory.LogoutMonster;
import monster.update.pageFactory.UpdateMonster;

public class AllInUpdatesMonster {

	Login_monster lm=PageFactory.initElements(Driver.driver,Login_monster.class);
	UpdateMonster um=PageFactory.initElements(Driver.driver,UpdateMonster.class);
	LogoutMonster lom=PageFactory.initElements(Driver.driver,LogoutMonster.class);
	
	
	CommonClasses cc=new CommonClasses();
	
	public void login() throws InterruptedException, AWTException{
		
		Driver.driver.get("http://www.monsterindia.com/");
		lm.signIn().click();
		
		lm.userName().sendKeys("jyotiranjan976@gmail.com");
		
		
		Thread.sleep(1000);
		cc.getChildClosed();
		Thread.sleep(1000);
		//cc.robo().keyPress(KeyEvent.VK_TAB);
		//lm.password().sendKeys("hritik");
		//cc.accept();
		
		
		cc.robo().keyPress(KeyEvent.VK_TAB);
		cc.robo().keyRelease(KeyEvent.VK_TAB);
		Thread.sleep(2000);
		cc.robo().keyPress(KeyEvent.VK_H);
		cc.robo().keyRelease(KeyEvent.VK_H);
		cc.robo().keyPress(KeyEvent.VK_R);
		cc.robo().keyRelease(KeyEvent.VK_R);
		cc.robo().keyPress(KeyEvent.VK_I);
		cc.robo().keyRelease(KeyEvent.VK_I);
		cc.robo().keyPress(KeyEvent.VK_T);
		cc.robo().keyRelease(KeyEvent.VK_T);
		cc.robo().keyPress(KeyEvent.VK_I);
		cc.robo().keyRelease(KeyEvent.VK_I);
		cc.robo().keyPress(KeyEvent.VK_K);
		cc.robo().keyRelease(KeyEvent.VK_K);
		lm.submit().click();
	}
	public void updateResume() throws InterruptedException, AWTException{
		
		um.updateProfile().click();
		um.editResume().click();
		Thread.sleep(2000);
		um.chooseFile().click();
		Thread.sleep(2000);
		cc.robo().keyPress(KeyEvent.VK_A);
		cc.robo().keyRelease(KeyEvent.VK_A);
		cc.robo().keyPress(KeyEvent.VK_U);
		cc.robo().keyRelease(KeyEvent.VK_U);
		Thread.sleep(1000);
		cc.robo().keyPress(KeyEvent.VK_DOWN);
		cc.robo().keyRelease(KeyEvent.VK_DOWN);
		Thread.sleep(1000);
		cc.robo().keyPress(KeyEvent.VK_ENTER);
		cc.robo().keyRelease(KeyEvent.VK_ENTER);
		cc.robo().keyPress(KeyEvent.VK_ENTER);
		cc.robo().keyRelease(KeyEvent.VK_ENTER);
		um.submitButton().click();
	}public void logout() throws InterruptedException{
		
		cc.moveToElement(lom.logoutImg());
		Thread.sleep(1000);
		lom.logout().click();
	}
}

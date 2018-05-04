package monster.update.testCases;

import java.awt.AWTException;

import org.testng.annotations.Test;

import com.update.businessClass.AllInUpdatesMonster;

public class Login_Mon {

	AllInUpdatesMonster aum=new AllInUpdatesMonster();
	
	@Test
	public void login() throws InterruptedException, AWTException{
		aum.login();
		aum.updateResume();
		aum.logout();
	}
}

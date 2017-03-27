package monster.update.testCases;

import org.testng.annotations.Test;

import com.update.businessClass.AllInUpdatesMonster;

public class Login_Mon {

	AllInUpdatesMonster aum=new AllInUpdatesMonster();
	
	@Test
	public void login() throws InterruptedException{
		aum.login();
	}
}

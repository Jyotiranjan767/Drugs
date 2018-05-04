package com.luckie.jax.messenger.service;

import java.util.ArrayList;
import java.util.List;

import com.luckie.jax.messenger.model.Messages;

public class Service {

	public List<Messages> getAllMessages(){

		Messages m1=new Messages(1L, "icant have that", "Sunny");
		Messages m2=new Messages(2L, "you may have that",  "Samantha");
		Messages m3=new Messages(3L, "all can  do that",  "Jonny");
		Messages m4=new Messages(4L, "nobody has done  that", "Xander");
	
		List<Messages> msg=new ArrayList<>();
		msg.add(m1);
		msg.add(m2);
		msg.add(m3);
		msg.add(m4);
        return msg;
	}
}

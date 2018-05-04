package com.luckie.jax.messenger.message;

import java.util.List;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import com.luckie.jax.messenger.model.Messages;
import com.luckie.jax.messenger.service.Service;

@Path("/messages")
public class Message1 {

	@GET
	@Produces(MediaType.APPLICATION_XML)
	public List<Messages> getMessage(){
		
	//return "Fuck you!";
		return new Service().getAllMessages();
	}
}

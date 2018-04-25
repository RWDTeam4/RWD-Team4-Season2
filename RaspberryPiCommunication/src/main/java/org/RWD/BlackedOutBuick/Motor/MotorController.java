package org.RWD.BlackedOutBuick.Motor;

import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@RestController
public class MotorController {
	
	@RequestMapping(value="/getMotorValues", method=RequestMethod.GET)
	public String getMotorValues(HttpServletRequest request, HttpServletResponse response){
		return "ValuesSent!";
	}
}
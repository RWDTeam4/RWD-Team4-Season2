/*
 * BaseWebServer.h
 *
 *  Created on: 19 Apr 2018
 *      Author: pi
 */
//
//#ifndef BASEWEBSERVER_H_
//#define BASEWEBSERVER_H_



#include "pistache/endpoint.h"
//#include "pistache/pistache.h"
using namespace Pistache;

class BaseWebServer : public Http::Handler {
public:
	HTTP_PROTOTYPE(BaseWebServer)

//	BaseWebServer();
//	virtual ~BaseWebServer();

	void onRequest(const Http::Request& request, Http::ResponseWriter response){
		response.send(Http::Code::Ok, "Hello, Dawg, What's Up?");
	}
};

int main() {
	Pistache::Address addr(Pistache::Ipv4::any(),
			Pistache::Port(9080));
	auto opts = Pistache::Http::Endpoint::options()
	        .threads(1);

	    Http::Endpoint server(addr);
	    server.init(opts);
	    server.setHandler(Http::make_handler<BaseWebServer>());
	    server.serve();
	    server.shutdown();
}

//#endif /* BASEWEBSERVER_H_ */



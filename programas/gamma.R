plotGamma=function(lb=0,ub=10,alfa=1,beta=1){
	xAxis=seq(lb,ub,len=300)
	yAxis=dgamma(xAxis,shape=alfa,scale=beta)
	title=paste("Funcion gamma con alfa= ",round(alfa,2)," y beta= ",round(beta,2),sep="")
	plot(xAxis,yAxis,type="l",main=title)
}

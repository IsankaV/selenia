account = {
	"Username":"IsankaV",
	"Password":"jacksparrow21352"
}
license = "x"
tradeset = {
	"BaseTrade":"0.01",
	"C1":"36", 							#5-95
	"C2":"48", 							#5-95
	"TradeCount":"5", 				#max limit 200
	"MultiplyOnWin":"0", 				## 0 untuk OFF 
	"MultiplyOnLose":"1", 				## 0 untuk OFF 
	"MaxBaseTrade":{
		"Toogle":"OFF",						#ON/OFF
		"Max":"0.9",
		"ResetOnLoseMaxTrade":"ON", 		# ON/OFF
		"StopOnLoseMaxTrade":"OFF"},			# ON/OFF
	"ClientSeed":"14476798",				#max 32 digits
}

tools = {
	"AddDelayTrade":"0",				#Delay Per Trade
	"AddDelayTradeWin":"0",				#Delay Per Trade Win
	"AddDelayTradeLose":"0",				#Delay Per Trade Lose
	"RecoveryMultiplier":"2",			# 1 untuk OFF. BaseTrade Lose Terakhir di Kali RecoveryMultiplier
	"RecoveryIncrease":"0",	 			# 0 untuk OFF. BaseTrade Lose Terakhir di Tambah RecoveryIncrease
	"TargetProfit":"50",				#0 untuk OFF
	"StopLoseBalance":"0", 				#0 untuk OFF
	"ForceTC1AfterLose":"ON",			#ON/OFF
	"ChangeTCAfterLose":{
		"Toogle":"OFF",
		"ChangeTo":"10"},
	"ContinueLastBase":"ON"			#ON/OFF. Fungsinya Kalau Lose Ingin Lanjutkan Base Terakhir atau Tidak		
}

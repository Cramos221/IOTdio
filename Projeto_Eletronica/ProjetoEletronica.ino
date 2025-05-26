
const int sensor = A0;
const int motor = 7;
const int LED = 2;
const int buzz = 5;
float temperatura = 0;


void setup()
{
	Serial.begin(9600);
    pinMode(motor, OUTPUT);
    pinMode(LED, OUTPUT);
    pinMode(buzz, OUTPUT);
	
}

void loop()
{

	temperatura = (analogRead(sensor) );
    float tensao = temperatura * (5.0 / 1023.0);
    float temperaturaCelsius = (tensao - 0.5) * 100.0;
    
    if(temperaturaCelsius >= 30 & temperaturaCelsius < 50 ){
      digitalWrite(motor, HIGH);
      delay(1000);
    }else if(temperaturaCelsius > 50) {
    digitalWrite(motor, HIGH);
    digitalWrite(LED, HIGH);
    digitalWrite(buzz, HIGH);
    }else{
    digitalWrite(motor, LOW);
    digitalWrite(LED, LOW);
    digitalWrite(buzz, LOW);
    
    }
    
    
    
  
   Serial.print("Temperatura = "); //IMPRIME O TEXTO NA SERIAL
   Serial.print(temperaturaCelsius); //IMPRIME NA SERIAL A TEMPERATURA MEDIDA
   Serial.println(" C"); //IMPRIME O TEXTO NA SERIAL
   delay(2000); //INTERVALO DE 2 SEGUNDOS
    }

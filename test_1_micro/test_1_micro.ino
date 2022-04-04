#define TAILLE_TAB 100000

bool tableau[TAILLE_TAB];
int i = 0;
bool kerblo = 0;

void IRAM_ATTR fonction_ISR() {
  //ets_printf
  if (i < TAILLE_TAB) {
    tableau[i] = digitalRead(34);
    i += 1;
  }

}

void setup() {
  // put your setup code here, to run once:
  pinMode(34, INPUT);
  pinMode(35, INPUT);
  Serial.begin(9600);
  attachInterrupt(35, fonction_ISR, RISING);

}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println(i);
  delay(1);
  if (i >= TAILLE_TAB && !kerblo) {
    kerblo = true;
    i = 0;
    for (int j = 0; j < TAILLE_TAB; j++) {
      Serial.println(tableau[j]);
    }
  }
}

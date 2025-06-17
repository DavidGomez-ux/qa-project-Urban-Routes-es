from codigo import retrieve_phone_code
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import phone_number, address_to


#Conocer los elementos de la página, cada elemento contiene el localizador
class UrbanRoutesPage:
    campo_desde = (By.XPATH, '//input[@id="from"]')
    campo_hasta = (By.XPATH, '//input[@id="to"]')
    modo_personal = (By.XPATH, '//div[@class = "mode" and contains(text(),"Personal")]')
    boton_pedir_taxi = (By.XPATH, "//button[@class='button round' and text()='Pedir un taxi']")
    tarifa_confort = (By.XPATH, '//div[text() = "10"]')
    boton_agregar_numero = (By.XPATH, '//div[@class="np-button"]')  # Botón para iniciar ingreso de número
    texto_agregar_numero = (By.XPATH, '//div[@class="np-text"]')
    campo_numero_input = (By.XPATH, '//div[@class="np-input"]/div')
    campo_escribir_numero = (By.ID, 'phone')
    boton_enviar_numero = (By.CLASS_NAME, "button.full")
    campo_codigo_telefono = (By.ID, 'code')
    boton_confirmar_codigo = (By.CSS_SELECTOR, '.section.active>form>.buttons>:nth-child(1)')
    boton_agregar_metodo_pago = (By.XPATH, '//div[contains(@class,"pp-text")]/..')
    seleccionar_pago_con_tarjeta = (By.XPATH, '//img[contains(@class,"pp-plus")]')
    campo_numero_tarjeta = (By.XPATH, '//input[contains(@id,"number")]')
    campo_codigo_tarjeta = (By.XPATH, '//input[contains(@name,"code")]')
    espacio_entre_codigo_y_boton_agregar = (By.XPATH, '//div[@class="card-wrapper"]')
    boton_agregar_tarjeta = (By.XPATH, '//div[@class="pp-buttons"]/button[@type="submit"]')
    boton_cerrar_metodos_pago = (By.XPATH, '(//button[@class="close-button section-close"])[3]')
    campo_mensaje = (By.XPATH, '//input[@name="comment"]')
    boton_manta_y_pañuelos = (By.XPATH, '(//span[@class="slider round"])[1]')
    boton_helados = (By.XPATH, '(//div[@class="counter-plus"])[1]')
    verificar_boton_final = (By.XPATH, '//span[@class= "smart-button-main" and contains(text(), "Pedir un taxi")]')
    contador_taxi = (By.CLASS_NAME, "order-btn-group")

    def __init__(self, driver):
        self.driver = driver


    # Se va a buscar seleccionar una ruta.
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

        # Definimos el metodo para llenar el campo desde
    def desde(self, address_from):
        txt_campo_desde = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.campo_desde))
        txt_campo_desde.send_keys(address_from)

        # Definimos el metodo para llenar el campo hasta
    def hasta(self, address_to):
        txt_campo_hasta = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.campo_hasta))
        txt_campo_hasta.send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.campo_desde).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.campo_hasta).get_property('value')

    # Rellenar los campos desde y hasta
    def set_rutas(self, address_from, address_to):
        self.desde(address_from)
        self.hasta(address_to)

        assert self.get_from() == address_from
        assert self.get_to() == address_to

     # Definimos el método para dar clic en el modo "Personal"

    def clic_boton_para_personal(self):
        clic_personal = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.modo_personal))
        clic_personal.click()

    # Seleccionar formato para "Pedir un taxi"
    def pedir_taxi(self):
        boton = self.driver.find_element(*self.boton_pedir_taxi)
        boton.click()

    # Seleccionar la tarifa confort
    def seleccionar_la_tarifa_confort(self):
        elemento = self.wait_for_element(self.tarifa_confort)
        elemento.click()

    def set_tarifa_comfort(self):
        self.clic_boton_para_personal()
        self.pedir_taxi()
        self.seleccionar_la_tarifa_confort()


    # Llenado del número de teléfono
    def click_agregar_numero(self):
        self.driver.find_element(*self.boton_agregar_numero).click()

    # Agregar número
    def click_campo_numero(self):
        self.driver.find_element(*self.campo_numero_input).click()

    # Ingresar Teléfono
    def ingresar_numero_telefono(self, phone_number):
        self.driver.find_element(*self.campo_escribir_numero).send_keys(phone_number)

    # Hacer click en botón enviar número
    def click_boton_enviar_numero(self):
        self.driver.find_element(*self.boton_enviar_numero).click()

    # Realizar código de teléfono
    def ingresar_codigo_telefono(self):
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.campo_codigo_telefono).send_keys(code)

    # Botón de confirmación de código
    def click_boton_confirmar_codigo(self):
        self.driver.find_element(*self.boton_confirmar_codigo).click()

    # Obtener número
    def obtener_texto_numero(self):
        return self.driver.find_element(*self.texto_agregar_numero).text

    # Full teléfono
    def completar_numero_telefono(self, phone_number):
        self.click_agregar_numero()
        self.click_campo_numero()
        self.ingresar_numero_telefono(phone_number)
        self.click_boton_enviar_numero()
        self.ingresar_codigo_telefono()
        self.click_boton_confirmar_codigo()


# Definimos el metodo para dar clic en el campo metodo de pago
    def clic_metodo_de_pago(self):
        clic_metodo_de_pago = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.boton_agregar_metodo_pago))
        clic_metodo_de_pago.click()

    # Definimos el metodo para dar clic en agregar medio de pago en tarjeta
    def medio_de_pago_tarjeta(self):
        clic_agregar_tarjeta = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.seleccionar_pago_con_tarjeta))
        clic_agregar_tarjeta.click()

    # Definimos el metodo para escribir el número de la tarjeta
    def numero_de_tarjeta(self, card_number):
        escribir_numero_de_tarjeta = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.campo_numero_tarjeta))
        escribir_numero_de_tarjeta.send_keys(card_number)

    # Definimos el metodo para obtener el número de la tarjeta
    def numero_de_la_tarjeta(self):
        return self.driver.find_element(*self.campo_numero_tarjeta).get_property('value')

    # Definimos el metodo para escribir el código de la tarjeta
    def codigo_de_tarjeta(self, card_code):
        escribir_codigo_de_tarjeta = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.campo_codigo_tarjeta))
        escribir_codigo_de_tarjeta.send_keys(card_code)

     # Definimos el metodo para obtener el código de la tarjeta
    def codigo_de_la_tarjeta(self):
        return self.driver.find_element(*self.campo_codigo_tarjeta).get_property('value')

    # Definimos el metodo para dar clic en cualquier parte de la pantalla para habilitar el botón agregar tarjeta
    def dar_clic_en_cualquier_parte_de_la_pantalla(self):
        clic_en_la_pantalla = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.espacio_entre_codigo_y_boton_agregar))
        clic_en_la_pantalla.click()

    # Definimos el metodo para dar clic en el botón agregar
    def agregar_tarjeta (self):
        clic_agregar = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.boton_agregar_tarjeta))
        clic_agregar.click()

    # Definimos el metodo para dar click en el boton cerrar la ventana del metodo de pago
    def metodo_de_pago(self):
        clic_boton_cerrar = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.boton_cerrar_metodos_pago))
        clic_boton_cerrar.click()

    '''
    Para ingresar la tarjeta como medio de pago, hacemos:
    1. clic el campo método de pago
    2. clic en agregar tarjeta
    3. escribir número de tarjeta.
    4. escribir código de la tarjeta.
    5. clic en cualquier zona de la pantalla.
    6. clic en el botón agregar.
    7. clic en el botón cerrar.
    '''

    def set_seleccionar_metodo_de_pago_tarjeta (self, card_number, card_code):
         self.clic_metodo_de_pago()
         self.medio_de_pago_tarjeta()
         self.numero_de_tarjeta(card_number)
         self.codigo_de_tarjeta(card_code)
         self.dar_clic_en_cualquier_parte_de_la_pantalla()
         self.agregar_tarjeta ()
         self.metodo_de_pago()


    # Enviar mensaje al conductor
    def escribir_mensaje_conductor(self, message_for_driver):
        self.driver.find_element(*self.campo_mensaje).send_keys(message_for_driver)

    # Solicitar manta y pañuelos
    def solicitar_manta_y_pañuelos(self):
        self.driver.find_element(*self.boton_manta_y_pañuelos).click()

    # Solicitar helados
    def solicitar_helados(self):
        boton = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.boton_helados))
        boton.click()

    # Definimos el metodo para dar clic en el botón final de pedir un taxi

    def check_boton_pedir_taxi_enabler(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.verificar_boton_final)).is_enabled()

        # Definimos el metodo para dar clic en el botón final de pedir un taxi

    def clic_boton_final_pedir_un_taxi(self):
        clic_boton_pedir_un_taxi = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.verificar_boton_final))
        clic_boton_pedir_un_taxi.click()

        # Definimos un metodo conocer si el contador del taxi está visible

    def check_espera_contador(self):
        return WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.contador_taxi)).is_displayed()
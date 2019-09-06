#include "user_main.h"
#include "ov2640_dcmi_drv.h"

void user_code1() {
}

void user_code2() {

	//  BSP_CAMERA_Init(IMAGE_RESOLUTION)
	// initiation camera
	ov2640_dcmi_drv &cam_driver = ov2640_dcmi_drv::instance();
	int i = 0;

	/* GPIOC & PIN 2 to measure execution time of CAMERA_Init function*/

//	while (1) {
//		GPIOG->BSRR |= GPIO_BSRR_BR_12;
//
//		GPIOC->BSRR |= GPIO_BSRR_BS_2; // GPIO_OUT_PUT = HIGH , turn off camera
//		do {
//			GPIOC->BSRR |= GPIO_BSRR_BR_2; // GPIO_OUT_PUT = LOW , turn on camera
//		} while (ov2640_ReadID(0x60) != OV2640_ID);
//		Camera_StatusTypeDef cam_status = cam_driver.CAMERA_Init(IMAGE_RESOLUTION);
//		GPIOG->BSRR |= GPIO_BSRR_BS_12;
//	}
	Camera_StatusTypeDef cam_status = cam_driver.CAMERA_Init(IMAGE_RESOLUTION);

	while (i < 5)
		switch (cam_status) {
		case CAMERA_OK:
			//  BSP_CAMERA_SnapshotStart(image_data);
			cam_driver.CAMERA_Resume();
			cam_driver.CAMERA_SnapshotStart(CAMERA_BUFFER_EXTERN);
			cam_driver.CAMERA_Stop();

			while (!uart_complete) {
			}
			uart_complete = 0;
			i++;
			break;
		case CAMERA_TIMEOUT:
			SEGGER_RTT_printf(0, "%s\n", "CAMERA_TIME_OUT");
			break;
		case CAMERA_ERROR:
			SEGGER_RTT_printf(0, "%s\n", "CAMERA_ERROR");
			break;
		}

}

void user_code3() {
	//GPIO_PinState pin_state = HAL_GPIO_ReadPin(GPIOC, GPIO_PIN_3);
	while (HAL_GPIO_ReadPin(GPIOC, GPIO_PIN_3) != GPIO_PIN_SET) {
	}
	//user_code2();
	SEGGER_RTT_printf(0, "%s\n", "snapshot start !!!\n");
}

void loop() {
	HAL_Delay(1000);
}

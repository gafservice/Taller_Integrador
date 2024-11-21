#include <Arduino.h>
#include "TaskRadiolib.h"

// Asegúrate de que USE_SX1268 esté definido
#define USE_SX1268

// Constructor
RadiolibTask::RadiolibTask(TaskQueue<std::shared_ptr<APRSMessage>> &fromModem, TaskQueue<std::shared_ptr<APRSMessage>> &_toModem)
    : Task("RadiolibTask", 0),  // Nombre de la tarea y ID de tarea
      _fromModem(fromModem),     // Inicializa las referencias
      _toModem(_toModem) {       // Inicializa las referencias
    // Inicialización adicional si es necesario
}

// Método de inicio
void RadiolibTask::begin(System &system) {
    // Código de inicialización para el sistema
}

// Manejo de errores de decodificación
void RadiolibTask::decodeError(System &system, int16_t state) {
    // Manejo de errores; reemplaza "Current Time" con el método adecuado para obtener el tiempo
    system.getLogger().log(logging::LoggerLevel::LOGGER_LEVEL_ERROR, getName(), "[%s] Packet too long.", "Current Time");

    // Manejo de estados
    switch (state) {
        default:
            system.getLogger().log(logging::LoggerLevel::LOGGER_LEVEL_ERROR, getName(), "[%s] Unknown state.", "Current Time");
            break;
    } 
}

// Método del bucle
bool RadiolibTask::loop(System &system) {
    // Código del bucle aquí
    return true; // Cambiar por la lógica apropiada
}

// Fin del archivo


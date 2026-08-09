| Función             | Tipo         | Datos de entrada                              | Resultado esperado                   |
| ------------------- | ------------ | --------------------------------------------- | ------------------------------------ |
| `validar_cedula`    | Normal       | `"1712345678"`                                | `Cédula Correcta`                               |
| `validar_cedula`    | Límite       | `"1234567890"` exactamente 10 dígitos         | `Cédula Correcta`                               |
| `validar_cedula`    | Error        | `"17123"`                                     | `Cédula Incorrecta`                              |
| `validar_fecha`     | Normal       | `"03/08/2026"`                                | `Fecha Correcta`                               |
| `validar_fecha`     | Límite       | `"31/01/2026"`                                | `Fecha Correcta`                               |
| `validar_fecha`     | Error        | `"31/02/2026"`                                | `Fecha Incorrecta`                              |
| `clasificar_tiempo` | Normal       | `20`                                          | `"Normal"`                           |
| `clasificar_tiempo` | Límite       | `10`                                          | `"Ágil"`                             |
| `clasificar_tiempo` | Error        | `-1`                                          | Lanza `ValueError`                   |
| `calcular_promedio` | Normal       | `[10, 20, 30]`                                | `20.0`                               |
| `calcular_promedio` | Límite       | `[10]`                                        | `10.0`                               |
| `calcular_promedio` | Error/Límite | `[]`                                          | `0.0`                                |
| `resumen_diario`    | Normal       | Registros con cédula, fecha y minutos válidos | Procesa los registros correctamente  |
| `resumen_diario`    | Límite       | Un solo registro válido                       | Total `1` y promedio correspondiente |
| `resumen_diario`    | Error        | Registro con cédula inválida                  | Se incrementa `descartados`          |

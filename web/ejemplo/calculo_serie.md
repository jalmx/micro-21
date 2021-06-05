# Calculo de circuito serie con Resistencias

 <p style="text-align: center;">
            <img src="https://www.areatecnologia.com/electricidad/imagenes/circuitos-serie.jpg" alt="circuito">
</p>
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Eveniet natus suscipit architecto, aut itaque, fugit, ratione quaerat recusandae fugiat ea voluptate nesciunt minima officiis. Sunt minima id enim saepe perspiciatis?

Earum sunt similique tenetur deleniti provident ab, officiis veritatis fuga perspiciatis cupiditate accusantium possimus laudantium deserunt quae voluptatibus iure vitae nulla ex alias quo, cumque nam. Esse totam assumenda explicabo!

Reprehenderit corrupti excepturi similique fuga accusantium? Excepturi facere corrupti rerum minus deleniti praesentium ut dicta nesciunt harum aliquid veritatis doloribus repellendus, mollitia id assumenda architecto distinctio, tenetur numquam, voluptatum voluptates?
Excepturi fuga molestiae mollitia quo? Consequuntur rem optio, consectetur facilis, doloremque exercitationem non esse quaerat harum id dolor qui in, quasi velit ducimus ipsum commodi deserunt blanditiis libero a. Nemo!

Deserunt maiores saepe quam cumque ipsam perferendis, dolorum eum veritatis adipisci temporibus ab beatae tenetur atque ea earum quasi sequi corrupti animi dicta ut aut officiis culpa sapiente necessitatibus. Nobis.

Officia accusantium porro quasi sequi, eos, dolorum magnam doloribus amet iusto fugiat ipsum in, saepe quia labore earum reiciendis. Hic, reiciendis labore! Iusto eos ullam doloremque, impedit quidem numquam autem?

Provident possimus sed dolorem est molestias quae perspiciatis magnam numquam, quasi fugit nulla in accusantium nobis. Magnam ullam est impedit culpa aperiam magni tempora illo. Quidem ipsa corporis soluta sunt.

Harum ipsum ipsa perferendis delectus in obcaecati ducimus dolorum magni minus, architecto, suscipit blanditiis et enim. Provident aspernatur repudiandae nemo saepe, sed ullam! Voluptatum aut quos dolorum pariatur laborum? Itaque.

Ratione, vitae nisi dignissimos, repudiandae harum adipisci quibusdam doloribus reiciendis accusamus a quae ullam corrupti accusantium alias aliquam rerum ipsam dicta necessitatibus! Nulla culpa non labore laudantium repudiandae sapiente veritatis.


```python
from pyfirmata import Arduino    #importamos la libreria que nos permite conectarnos por el protocolo de firmata
import time         # importamos la libreria de retardos

# Indicamos el puerto donde se encuentra conectada la tarjeta electronica
PORT = 'COM#'
board = Arduino(PORT) 

board.digital[3].write(1) #se manda un nivel 1 a la salida del pin 3
time.sleep(5)             #nos esperamos un sengundo
board.digital[3].write(0) #se manda un nivel 0 a la salida del pin 3
time.sleep(5)             #nos esperamos un sengundo
board.digital[3].write(1) #se manda un nivel 1 a la salida del pin 3
```

---

[Ir al inicio](index.html)
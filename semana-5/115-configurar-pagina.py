def configurar_pagina(**kwargs):
    tema = kwargs.get("tema","claro")
    idioma = kwargs.get("idioma","español")
    print(f"Configuración -> tema {tema}, idioma {idioma}")

configurar_pagina(tema="oscuro")
configurar_pagina()

.. _verkefni8:

Verkefni 8
==========

Nú skulum við setja þak á húsið. Til að vita hvar þakið á að fara þurfum við fyrst að vita hversu hátt húsið er og bæta þakinu ofan á það.


.. image:: /images/cube-roof.jpg

Ímyndum okkur nú að þetta sé húsið sem við smíðuðum. Skoðaðu vel breytuna *thak_byrjar*. Þar erum við að ákveða á hvaða hniti þakið byrjar.


.. code-block:: python
    
    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()

    hnit = mc.player.getTilePos()


    x = hnit.x + 3
    y = hnit.y
    z = hnit.z + 3

    print(x, y, z)


    lengd = 10
    breidd = 10
    haed = 10

    # Smíða hús
    mc.setBlocks(x, y, z, x + lengd, y + haed, z + breidd, 1)

    lengd_loft = 8
    breidd_loft = 8
    haed_loft= 8

    x_loft = x + 1
    y_loft = y + 1
    z_loft = z + 1

    # Búa til loft kubba innan í húsið
    mc.setBlocks(x_loft, y_loft, z_loft, x_loft + lengd_loft, y_loft + haed_loft, z_loft + breidd_loft, 0)


    thak_byrjar = y + haed

    # Smíða þak ofan á húsið
    mc.setBlocks(x, thak_byrjar, z, x + lengd, thak_byrjar + 5, z + breidd, 5)




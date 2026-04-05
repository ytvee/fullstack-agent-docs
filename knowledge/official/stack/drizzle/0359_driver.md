### `driver`
<rem025/>

Drizzle Kit automatically picks available database driver from your current project based on the provided `dialect`, 
yet some vendor specific databases require a different subset of connection params.

`driver` option let's you explicitely pick those exceptions drivers.

|               |                      |
| :------------ | :-----------------   |
| type          | <Drivers/> |
| default        | --                    |
| commands      | `migrate` `push` `pull`   |

<rem025/>

<DriversExamples/>


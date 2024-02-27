"""Sensor platform for integration_blueprint."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription, SensorStateClass
from homeassistant.helpers.entity import EntityCategory
from homeassistant.const import (
    UnitOfElectricPotential,
    DEVICE_CLASS_VOLTAGE,
)

from .const import (
    DOMAIN,
    LOGGER,
    SENSORS,
    SENSOR_KEY,
    SENSOR_ATTRS,
    SENSOR_CATEGORY,
)
from .coordinator import BlueprintDataUpdateCoordinator
from .entity import IntegrationBlueprintEntity


ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="battVoltage",
        name=DOMAIN+"_Battery Voltage",
        icon="mdi:battery",
        device_class= DEVICE_CLASS_VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement=UnitOfElectricPotential.VOLT
    ),
    SensorEntityDescription(
        key="mode",
        name=DOMAIN+"Pack mode",
        icon="mdi:auto-mode",
    ),
    SensorEntityDescription(
        key="theme",
        name=DOMAIN+"Pack Theme",
        icon="mdi:theme-light-dark",
    ),
    SensorEntityDescription(
        key="cyclotron",
        name=DOMAIN+"Cyclotron state",
        icon="mdi:sync",
    ),
        SensorEntityDescription(
        key="firing",
        name=DOMAIN+"Firing State",
        icon="mdi:flash",
    ),
        SensorEntityDescription(
        key="wand",
        name=DOMAIN+"Wand State",
        icon="mdi:magic-staff",
    ),
        SensorEntityDescription(
        key="wandMode",
        name=DOMAIN+"Firing Mode",
        icon="mdi:gamepad-outline",
    ),
        SensorEntityDescription(
        key="wandPower",
        name=DOMAIN+"Wand Firing State",
        icon="mdi:fire",
    ),
        SensorEntityDescription(
        key="temperature",
        name=DOMAIN+"Overheat state",
        icon="mdi:radiator",
    ),
        SensorEntityDescription(
        key="switch",
        name=DOMAIN+"Pack Armed",
        icon="mdi:arm-flex",
    ),
        SensorEntityDescription(
        key="safety",
        name=DOMAIN+"Wand Armed",
        icon="mdi:radiator",
    ),
        SensorEntityDescription(
        key="pack",
        name=DOMAIN+"Pack State",
        icon="mdi:bag-personal",
    ),
        SensorEntityDescription(
        key="cable",
        name=DOMAIN+"Ribbon Cable",
        icon="mdi:cable-data",
    ),
        SensorEntityDescription(
        key="musicCurrent",
        name=DOMAIN+"Current Song",
        icon="mdi:music",
    ),
        SensorEntityDescription(
        key="musicEnd",
        name=DOMAIN+"Last Song",
        icon="mdi:music",
    ),
        SensorEntityDescription(
        key="musicStart",
        name=DOMAIN+"First Song",
        icon="mdi:music",
    ),
        SensorEntityDescription(
        key="volMusic",
        name=DOMAIN+"Music Volume",
        icon="mdi:volume-high",
    ),
        SensorEntityDescription(
        key="volEffects",
        name=DOMAIN+"Effect Volume",
        icon="mdi:volume-high",
    ),
        SensorEntityDescription(
        key="volMaster",
        name=DOMAIN+"Master Volume",
        icon="mdi:volume-high",
    ),
        SensorEntityDescription(
        key="power",
        name=DOMAIN+"Firing Intensity",
        icon="mdi:knob",
    ),
)

WIFI_ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="enabled",
        name=DOMAIN+"wifi_enabled",
        icon="mdi:wifi",
        entity_category=EntityCategory.DIAGNOSTIC
    ),
    SensorEntityDescription(
        key="network",
        name=DOMAIN+" nework",
        icon="mdi:console-network",
        entity_category=EntityCategory.DIAGNOSTIC
    ),
    SensorEntityDescription(
        key="address",
        name=DOMAIN+" ip address",
        icon="mdi:ip-network",
        entity_category=EntityCategory.DIAGNOSTIC
    ),
)

SMOKE_ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="smokeEnabled",
        name=DOMAIN+" smoke enabled",
        icon="mdi:smoke",
        #entity_category=EntityCategory.DIAGNOSTIC
    ),
    SensorEntityDescription(
        key="smokeEnabled",
        name=DOMAIN+" smoke enabled",
        icon="mdi:smoke",
        #entity_category=EntityCategory.DIAGNOSTIC
    ),
)

# PACK_ENTITY_DESCRIPTIONS = (
#     SensorEntityDescription(
#         key="smokeEnabled",
#         name=DOMAIN+" smoke enabled",
#         icon="mdi:smoke",
#         #entity_category=EntityCategory.DIAGNOSTIC
#     ),
# )

# WAND_ENTITY_DESCRIPTIONS = (
#     SensorEntityDescription(
#         key="smokeEnabled",
#         name=DOMAIN+" smoke enabled",
#         icon="mdi:smoke",
#         #entity_category=EntityCategory.DIAGNOSTIC
#     ),
# )



async def async_setup_entry(hass, entry, async_add_devices):
    """Set up the STATUS sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id+"status"]
    print(entry)
    print(coordinator)
    print(DOMAIN)
    async_add_devices(
         IntegrationBlueprintSensor(
             coordinator=coordinator,
             entity_description=entity_description,
         )
         for entity_description in ENTITY_DESCRIPTIONS
    )
    print("status coordinator data")
    print(coordinator.data)

    """Set up the WIFI sensor platform."""
    wificoordinator = hass.data[DOMAIN][entry.entry_id+"wifi"]
    print(entry)
    print(wificoordinator)
    print(DOMAIN)
    async_add_devices(
         IntegrationBlueprintSensor(
             coordinator=wificoordinator,
             entity_description=entity_description,
         )
         for entity_description in WIFI_ENTITY_DESCRIPTIONS
    )
    print("wifi coordinator data")
    print(wificoordinator.data)

    """Set up the smoke sensor platform."""
    smokecoordinator = hass.data[DOMAIN][entry.entry_id+"smoke"]
    print(entry)
    print(smokecoordinator)
    print(DOMAIN)
    async_add_devices(
         IntegrationBlueprintSensor(
             coordinator=smokecoordinator,
             entity_description=entity_description,
         )
         for entity_description in SMOKE_ENTITY_DESCRIPTIONS
    )
    print("smoke coordinator data")
    print(smokecoordinator.data)

    # """Set up the WIFI sensor platform."""
    # wificoordinator = hass.data[DOMAIN][entry.entry_id+"pack"]
    # print(entry)
    # print(wificoordinator)
    # print(DOMAIN)
    # async_add_devices(
    #      IntegrationBlueprintSensor(
    #          coordinator=wificoordinator,
    #          entity_description=entity_description,
    #      )
    #      for entity_description in WIFI_ENTITY_DESCRIPTIONS
    # )
    # print("wifi coordinator data")
    # print(wificoordinator.data)

    # """Set up the WIFI sensor platform."""
    # wificoordinator = hass.data[DOMAIN][entry.entry_id+"wand"]
    # print(entry)
    # print(wificoordinator)
    # print(DOMAIN)
    # async_add_devices(
    #      IntegrationBlueprintSensor(
    #          coordinator=wificoordinator,
    #          entity_description=entity_description,
    #      )
    #      for entity_description in WIFI_ENTITY_DESCRIPTIONS
    # )
    # print("wifi coordinator data")
    # print(wificoordinator.data)




class IntegrationBlueprintSensor(IntegrationBlueprintEntity, SensorEntity):
    """integration_blueprint Sensor class."""

    def __init__(
        self,
        coordinator: BlueprintDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._attr_unique_id = entity_description.name
        #print("entity"+self.entity_description)
        #print()

    @property
    #def native_value(self) -> str:
    def native_value(self):
        """Return the native value of the sensor."""
        # return self.coordinator.data.get("mode")
        print(self.entity_description.key)
        print(self.coordinator.data)
        print(self.coordinator)
        #print(self.coordinator.data.get(self.entity_description.key))
        return self.coordinator.data.get(self.entity_description.key)


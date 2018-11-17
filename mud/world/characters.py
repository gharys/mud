import json


attributes = {"name","health", "stamina", "magic"}


class Character:
    def __init__(self, name, health, stamina, magic):
        self.__attributes = {"name": name, "health": health, "stamina": stamina, "magic": magic}
        self.__effects = set()

    def attribute(self, attr):
        value = self.__attributes[attr]
        for effect in self.__effects:
            value = effect.apply(attr, value)
        return value

    def health(self):
        return self.attribute("health")

    def add_effect(self, effect):
        self.__effects.add(effect)

    def as_dict(self):
        result = {}
        result.update(self.__attributes)
        result.update({"effects": [e.as_dict() for e in self.__effects]})
        return result

    def from_dict(character_dict):
        # attributen eruit halen
        attr = {k: character_dict[k] for k in attributes}
        result = Character(**attr)
        # effecten weer toewijzen
        effect_dicts = character_dict["effects"]
        for e in effect_dicts:
            effect = Effect.from_dict(e)
            result.add_effect(effect)
        return result


class Effect:
    def apply(self, attribute, value):
        pass

    def as_dict(self):
        pass

    def from_dict(effect_dict):
        type = effect_dict["type"]
        effect_dict.pop("type") # pop removes and returns last object from the list
        if type == "ModifyAttributeEffect":
            return ModifyAttributeEffect(**effect_dict)
        else:
            raise ValueError("Type unknown: "+type)


class ModifyAttributeEffect(Effect):
    def __init__(self, attribute, modifier):
        self.__attribute = attribute
        self.__modifier = modifier

    def apply(self, attribute, value):
        if attribute == self.__attribute:
            value = value + self.__modifier
        return value

    def as_dict(self):
        return {"type": "ModifyAttributeEffect",
                "attribute": self.__attribute,
                "modifier": self.__modifier}


c = Character("Fred", 200, 10, 5)
print (c.attribute("health"))
c.add_effect(ModifyAttributeEffect("health",
100))
c.add_effect(ModifyAttributeEffect("name", " arys"))
str = json.JSONEncoder().encode(c.as_dict())
copy_c = Character.from_dict(json.JSONDecoder().decode(str))
print(copy_c.health())
print(copy_c.attribute("name"))
print(c.__)

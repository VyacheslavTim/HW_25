from marshmallow import Schema, fields, validates, ValidationError

VALID_CMD_COMMANDS = ('filter', 'unique', 'limit', 'map', 'sort')


class RequestSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str()

    @validates
    def check_all_cmd_valid(self, values: dict[str, str], *args, **kwargs):
        if values['cmd'] not in VALID_CMD_COMMANDS:
            raise ValidationError('"cmd" contains invalid value')


class BatchRequestSchema():
    queries = fields.Nested(RequestSchema, many=True)
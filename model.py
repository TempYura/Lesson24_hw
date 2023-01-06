from marshmallow import Schema, ValidationError, fields, validates_schema
from config import CMD_TO_EXECUTE


class RequestSchema(Schema):
    cmd = fields.Str()
    value = fields.Str()

    @validates_schema
    def check_all_cmd_valid(self, values, *args, **kwargs):
        if values["cmd"] not in CMD_TO_EXECUTE.keys():
            raise ValidationError('"cmd" contains invalid value')

        if values["cmd"] == "sort" and values["value"] not in ["asc", "desc"]:
            raise ValidationError('sort value contains invalid string')

class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)
    filename = fields.Str()

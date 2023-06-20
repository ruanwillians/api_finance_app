from database import db
from src.model.expense import Expense
from database import db
from uuid import uuid4
from src.schema.expense import ExpenseSchema

expense_schema = ExpenseSchema(many=True)


class expenseRepository():

    def save(self, data):
        db.session.add(data)
        db.session.commit()

    def generate_item(seld, data):
        description = data['description']
        date = data['date']
        value = data['value']
        category_id = data['category_id']
        user_id = data['user_id']

        item = Expense(date=date, description=description,
                       value=value, category_id=category_id, user_id=user_id)

        return item

    def get_all(self, user_id, category_id, start_date, end_date):
        if user_id:
            if category_id:
                data = Expense.query.filter(
                    Expense.user_id == user_id,
                    Expense.category_id == category_id,
                    Expense.date >= start_date,
                    Expense.date <= end_date
                ).all()
            else:
                data = Expense.query.filter(
                    Expense.user_id == user_id,
                    Expense.date >= start_date,
                    Expense.date <= end_date
                ).all()
        else:
            data = Expense.query.filter(
                Expense.date >= start_date,
                Expense.date <= end_date
            ).all()

        if not data:
            return {'error': 'Expense not found'}
        else:
            serialized_data = expense_schema.dump(data)
            return serialized_data

    def get_by_id(self, id):
        data = Expense.query.filter_by(id=id).first()
        if not data:
            return {'error': 'Expense not found'}
        else:
            serialized_data = Expense.json(data)
            return serialized_data

    def create(self, data):
        item = self.generate_item(data)
        self.save(item)
        return item

    def edit_expense(self, id, data):
        expense = Expense.query.filter_by(id=id).first()
        if not expense:
            return {'error': 'User not found'}
        else:
            if 'description' in data:
                expense.description = data['description']
            if 'date' in data:
                expense.date = data['date']
            if 'value' in data:
                expense.value = data['value']
            if 'category_id' in data:
                expense.category_id = data['category_id']

            self.save(expense)
            serialized_data = Expense.json(expense)
            return serialized_data

    def delete_expense(self, id):
        expense = Expense.query.filter_by(id=id).first()

        if not expense:
            return {'error': 'expense not found'}

        db.session.delete(expense)
        db.session.commit()

        return {'message': 'expense deleted successfully'}

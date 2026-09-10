from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.permissions import IsAuthenticated


class ExpenseListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
          expenses = Expense.objects.filter(user=request.user)

          category = request.query_params.get('category')
    
          if category:
                  expenses = expenses.filter(category=category)

          serializer = ExpenseSerializer(expenses, many=True)
          return Response(serializer.data)

    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)

        if serializer.is_valid():
            expense = serializer.save(user=request.user)
            return Response(
                ExpenseSerializer(expense).data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request, pk):
        try:
            return Expense.objects.get(pk=pk, user=request.user)
        except Expense.DoesNotExist:
            return None

    def get(self, request, pk):
        expense = self.get_object(request, pk)

        if not expense:
            return Response(
                {"error": "Expense not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(ExpenseSerializer(expense).data)

    def put(self, request, pk):
        expense = self.get_object(request, pk)

        if not expense:
            return Response(
                {"error": "Expense not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ExpenseSerializer(
            expense,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        expense = self.get_object(request, pk)

        if not expense:
            return Response(
                {"error": "Expense not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        expense.delete()

        return Response(
            {"message": "Expense deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
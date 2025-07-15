from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader

def fine_tune_and_save():
    train_examples = [
        InputExample(texts=["What is AI?", "Artificial Intelligence course"], label=1.0),
        InputExample(texts=["Learn data science", "Data Science for Beginners"], label=0.8),
        InputExample(texts=["Can you suggest me some course in IT security", "IT security for Beginners"],label=0.8),


    ]

    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=8)
    train_loss = losses.CosineSimilarityLoss(model)
    model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=1)

    # Save the fine-tuned model
    model.save("./fine_tuned_model")

if __name__ == "__main__":
    fine_tune_and_save()
